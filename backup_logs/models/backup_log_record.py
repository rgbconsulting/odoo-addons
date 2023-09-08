# -*- coding: utf-8 -*-
# Copyright 2023 RGB Informàtica i Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import SUPERUSER_ID, models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import fnmatch
import subprocess
import logging

_logger = logging.getLogger(__name__)


def get_size_format(bsize, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if bsize < factor:
            return f'{bsize:.2f}{unit}{suffix}'
        bsize /= factor
    return f'{bsize:.2f}Y{suffix}'


class BackupLogRecord(models.Model):
    _name = 'backup.log.record'
    _description = 'Record representing the backup log line information'
    _order = 'id desc'

    date_registration = fields.Datetime(string='Date', default=lambda self: fields.Datetime.now())
    file_name = fields.Char(string='File', default=0)
    file_size = fields.Char(string='Size')
    message = fields.Char(string='Message')
    log_type_id = fields.Many2one(
        "backup.log.type", string="Type", index=True
    )

    @api.model
    def update_backup_logs(self):
        try:
            self.search_db_backups()
        except Exception as ex:
            _logger.error("ERROR: importing database backups. %s", ex)
        try:
            self.search_site_backups()
        except Exception as ex:
            _logger.error("ERROR: importing database backups. %s", ex)

    def search_db_backups(self):
        db_backup_type = self.env['backup.log.type'].search([('log_type', '=', 'db')], limit=1)
        if not db_backup_type:
            return

        type_baas = os.path.exists('/home/baas')
        current_db = self.env.cr.dbname
        last_record = self.env['backup.log.record'].search([('log_type_id', '=', db_backup_type.id)], order="id desc",
                                                           limit=1)
        if last_record:
            last_datetime = last_record.date_registration
        else:
            last_datetime = datetime.today() + relativedelta(months=-6)

        _logger.info("Importing databse backup logs since: %s", str(last_datetime))

        date_since_str = (last_datetime + relativedelta(hours=-2)).strftime('%Y-%m-%d %H:%M')
        log_lines = []

        p_journal = subprocess.Popen(["cat", "/var/log/syslog"], stdout=subprocess.PIPE)
        p_grep = subprocess.Popen(["grep", "db-odoo-backup"], stdin=p_journal.stdout, stdout=subprocess.PIPE)
        backup_logs_all = p_grep.stdout.read()
        if not backup_logs_all:
            p_journal = subprocess.Popen(["cat", "/var/log/syslog"], stdout=subprocess.PIPE)
            p_grep = subprocess.Popen(["grep", "lite-db-backup"], stdin=p_journal.stdout, stdout=subprocess.PIPE)
            backup_logs_all = p_grep.stdout.read()
        p_grep.stdout.close()
        p_journal.stdout.close()
        log_lines = backup_logs_all.splitlines()

        for log_line in log_lines:
            try:
                src_line = log_line.decode('ascii')
                t_date_array = src_line.split(']:', 1)[0].strip().split()
                t_datetime = datetime.strptime(
                    '{0} {1} {2} {3}'.format(datetime.now().year, t_date_array[0], t_date_array[1], t_date_array[2]),
                    '%Y %b %d %H:%M:%S')
                # Exclude those that have already been imported
                if t_datetime <= last_datetime:
                    continue
                if 'prod-' not in src_line:
                    continue
                src_line_splited_array = src_line.split(']:', 1)[1].strip().split()
                exec_file = src_line_splited_array[4]
                if exec_file:
                    instance_backup_dirs = os.listdir('/mnt/extra-storage/backup/odoo/')
                    t_backup_dir = ''
                    for backup_dir in instance_backup_dirs:
                        if (backup_dir in exec_file) and (backup_dir in current_db):
                            t_backup_dir = backup_dir
                            break
                    bkp_base_path = '/mnt/extra-storage/backup/odoo/{0}/prod-01'.format(t_backup_dir)
                    joined_time_str = ''.join(t_date_array[2].split(':'))

                    with os.scandir(bkp_base_path) as bkp_files:
                        for bkp_file in bkp_files:
                            if bkp_file.is_file():
                                t_old_style_dt_file_part_str = datetime.strftime(t_datetime, '%Y-%m-%d_%H-%M-%S')
                                t_dt_file_part_str = datetime.strftime(t_datetime, '%Y%m%d_%H%M%S')
                                # Valida que el fichero corresponda con el log por la hora
                                if (t_old_style_dt_file_part_str not in bkp_file.name) and \
                                        (t_dt_file_part_str not in bkp_file.name):
                                    continue
                                if bkp_file.name.startswith('db-') and (joined_time_str in bkp_file.name):
                                    bfile_size = bkp_file.stat().st_size
                                    vals = {
                                        "date_registration": t_datetime,
                                        "file_name": bkp_file.name,
                                        "file_size": get_size_format(bfile_size),
                                        "message": 'Instance {0} database backup'.format(t_backup_dir),
                                        "log_type_id": db_backup_type.id,
                                    }
                                    self.env['backup.log.record'].create(vals)
                                    break
            except Exception as e:
                _logger.error("ERROR: getting database backup logs: %s", e)
        return 0

    def search_site_backups(self):
        site_backup_type = self.env['backup.log.type'].search([('log_type', '=', 'site')], limit=1)
        if not site_backup_type:
            return

        type_baas = os.path.exists('/home/baas')
        current_db = self.env.cr.dbname
        last_record = self.env['backup.log.record'].search([('log_type_id', '=', site_backup_type.id)], order="id desc",
                                                           limit=1)
        if last_record:
            last_datetime = last_record.date_registration
        else:
            last_datetime = datetime.today() + relativedelta(months=-6)

        _logger.info("Importing site backup logs since: %s", str(last_datetime))

        date_since_str = (last_datetime + relativedelta(hours=-2)).strftime('%Y-%m-%d %H:%M')
        log_lines = []

        p_journal = subprocess.Popen(["cat", "/var/log/syslog"], stdout=subprocess.PIPE)
        p_grep = subprocess.Popen(["grep", "site-odoo-backup"], stdin=p_journal.stdout, stdout=subprocess.PIPE)
        backup_logs_all = p_grep.stdout.read()
        if not backup_logs_all:
            p_journal = subprocess.Popen(["cat", "/var/log/syslog"], stdout=subprocess.PIPE)
            p_grep = subprocess.Popen(["grep", "site-backup"], stdin=p_journal.stdout, stdout=subprocess.PIPE)
            backup_logs_all = p_grep.stdout.read()
        p_grep.stdout.close()
        p_journal.stdout.close()
        log_lines = backup_logs_all.splitlines()

        for log_line in log_lines:
            try:
                src_line = log_line.decode('ascii')
                t_date_array = src_line.split(']:', 1)[0].strip().split()
                t_datetime = datetime.strptime(
                    '{0} {1} {2} {3}'.format(datetime.now().year, t_date_array[0], t_date_array[1], t_date_array[2]),
                    '%Y %b %d %H:%M:%S')
                # Exclude those that have already been imported
                if t_datetime <= last_datetime:
                    continue
                if 'prod-' not in src_line:
                    continue
                src_line_splited_array = src_line.split(']:', 1)[1].strip().split()
                exec_file = src_line_splited_array[4]
                if exec_file:
                    instance_backup_dirs = os.listdir('/mnt/extra-storage/backup/odoo/')
                    t_backup_dir = ''
                    for backup_dir in instance_backup_dirs:
                        if (backup_dir in exec_file) and (backup_dir in current_db):
                            t_backup_dir = backup_dir
                            break
                    bkp_base_path = '/mnt/extra-storage/backup/odoo/{0}/prod-01'.format(t_backup_dir)
                    joined_time_str = ''.join(t_date_array[2].split(':'))

                    with os.scandir(bkp_base_path) as bkp_files:
                        for bkp_file in bkp_files:
                            if bkp_file.is_file():
                                t_old_style_dt_file_part_str = datetime.strftime(t_datetime, '%Y-%m-%d_%H-%M-%S')
                                t_dt_file_part_str = datetime.strftime(t_datetime, '%Y%m%d_%H%M%S')
                                # Valida que el fichero corresponda con el log por la hora
                                if (t_old_style_dt_file_part_str not in bkp_file.name) and \
                                        (t_dt_file_part_str not in bkp_file.name):
                                    continue
                                if bkp_file.name.startswith('odoo-') \
                                        or ((fnmatch.fnmatch(bkp_file.name, '*-site-*')
                                             or fnmatch.fnmatch(bkp_file.name, 'site-*'))
                                            and (joined_time_str in bkp_file.name)):
                                    bfile_size = bkp_file.stat().st_size
                                    vals = {
                                        "date_registration": t_datetime,
                                        "file_name": bkp_file.name,
                                        "file_size": get_size_format(bfile_size),
                                        "message": 'Instance {0} site backup'.format(t_backup_dir),
                                        "log_type_id": site_backup_type.id,
                                    }
                                    self.env['backup.log.record'].create(vals)
                                    break
            except Exception as e:
                _logger.error("ERROR: getting site backup logs: %s", e)
        return 0
