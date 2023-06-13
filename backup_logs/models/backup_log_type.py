# -*- coding: utf-8 -*-
# Copyright 2023 RGB Informàtica i Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import SUPERUSER_ID, models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class BackupLogType(models.Model):
    _name = 'backup.log.type'
    _description = 'Record representing the backup log type information'

    type_name = fields.Char(string='Name')
    log_type = fields.Selection(
        [('db', 'DB'), ('site', 'SITE')],
        string="Type",
        default="disk",
        help="Define where the backup is sent.\nDISK - Local disk\nBAAS - BaaS servers")
    output_dest = fields.Selection(
        [('disk', 'DISK'), ('baas', 'BAAS')],
        string="Destination",
        default="disk",
        help="Define where the backup is sent.\nDISK - Local disk\nBAAS - BaaS servers")
    directory = fields.Char(string='Directory')
    exec_interval_number = fields.Integer(string='Interval Number', default=1)
    exec_interval_unit = fields.Selection(
        [('mins', 'Minutes'), ('hours', 'Hours'), ('days', 'Days')],
        string="Interval Unit",
        default="hours",
        help="Define the execution interval of the Backup process.")
    available_disk = fields.Char(string='Available Disk')
    log_record_ids = fields.One2many(
        "backup.log.record", "log_type_id", string="Backup Log Records"
    )

    def open_logs_tree_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Backup Logs'),
            'res_model': 'backup.log.record',
            'view_type': 'tree',
            'view_mode': 'tree',
            'domain': [('log_type_id', '=', self.id)],
            'view_id': self.env.ref('backup_logs.backup_log_record_tree_view').id,
            'target': 'new',
        }
