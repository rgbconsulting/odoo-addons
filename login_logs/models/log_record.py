# -*- coding: utf-8 -*-
# Copyright 2023 RGB Informàtica i Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import SUPERUSER_ID, models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
import subprocess
import re
import logging

_logger = logging.getLogger(__name__)


class LogRecord(models.Model):
    _name = 'log.record'
    _description = 'Record representing de log line information'
    _order = 'id desc'

    # %(asctime)s %(pid)s %(levelname)s %(dbname)s %(name)s: %(message)s
    # fecha_hora, id_proceso, nivel o tipo, nombre_bd, nombre(modelo), mensaje
    date_registration = fields.Datetime(string='Date', default=lambda self: fields.Datetime.now(), readonly=True)
    process_id = fields.Integer(string='Process', default=0, readonly=True)
    level = fields.Char(string='Level', readonly=True)
    database_name = fields.Char(string='Database', readonly=True)
    model_name = fields.Char(string='Model Name', readonly=True)
    login_user = fields.Char(string='User', readonly=True)
    login_source_addr = fields.Char(string='Source', readonly=True)
    message = fields.Char(string='Message', readonly=True)

    @api.model
    def get_journalctl_login_logs(self):
        dt1_pattern = r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d*)\b'
        p_pattern = r'(\d{1,10})\b'
        t_pattern = r'(\D+)\s\b'
        db_pattern = r'([\w-]+)\s\b'
        m_full_pattern = r'([a-zA-Z_\.]+)\b'
        m_split_pattern = r'(?=[a-z0-1A-Z_\.-]+)login:'

        process_uid = self.env['ir.config_parameter'].with_user(SUPERUSER_ID).get_param('journal_process_uid')
        if not process_uid:
            process_uid = self.env.cr.dbname

        last_record = self.env['log.record'].search([], order="id desc", limit=1)
        if last_record:
            last_datetime = last_record.date_registration
        else:
            last_datetime = datetime.today() + relativedelta(months=-6)

        _logger.info("Importing login logs since: %s", str(last_datetime))

        date_since_str = (last_datetime + relativedelta(hours=-2)).strftime('%Y-%m-%d %H:%M')
        log_lines = []

        p_journal = subprocess.Popen(["journalctl", "--since", date_since_str, "--no-pager", "-u", process_uid],
                                     stdout=subprocess.PIPE)
        if p_journal:
            p_grep = subprocess.Popen(["grep", ": Login"], stdin=p_journal.stdout, stdout=subprocess.PIPE)
            login_logs_all = p_grep.stdout.read()
            p_grep.stdout.close()
            p_journal.stdout.close()
            log_lines = login_logs_all.splitlines()

        # TEST: Load data from file with only login logs lines
        #log_lines = []
        #with open('/opt/odoo/possala-15.0/test-logs.txt', 'r') as file:
        #    log_lines = file.read().splitlines()

        for log_line in log_lines:
            try:
                src_line = log_line.split(']:', 1)[1].strip()
                t_date = re.split(dt1_pattern, src_line)[1]
                t_datetime = datetime.strptime(t_date, '%Y-%m-%d %H:%M:%S,%f')
                # Exclude those that have already been imported
                if t_datetime <= last_datetime:
                    continue
                src_line = src_line[len(t_date) + 1:]
                t_process = re.split(p_pattern, src_line)[1]
                src_line = src_line[len(t_process) + 1:]
                t_type = re.split(t_pattern, src_line)[1]
                src_line = src_line[len(t_type) + 1:]
                t_dbname = re.split(db_pattern, src_line)[1]
                src_line = src_line[len(t_dbname) + 1:]
                t_model = re.split(m_full_pattern, src_line)[1]
                src_line = src_line[len(t_model) + 1:]
                t_full_message = src_line.strip()
                # Get message, user and source from full message
                t_message = re.split(m_split_pattern, t_full_message)[0].strip()
                t_full_message = re.split(m_split_pattern, t_full_message)[1]
                t_user = t_full_message.split()[0].strip()
                t_source = t_full_message.split()[2].strip()

                vals = {
                    "date_registration": t_datetime,
                    "process_id": int(t_process),
                    "level": t_type,
                    "database_name": t_dbname,
                    "model_name": t_model,
                    "login_user": t_user,
                    "login_source_addr": t_source,
                    "message": t_message,
                }
                self.env['log.record'].create(vals)
            except:
                _logger.error("Error getting Login log: %s", log_line)
