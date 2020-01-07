# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    worked_hours = fields.Float(string='Attended hours')
    error_attendances = fields.Boolean(default=False)
    notification_note = fields.Text(string='Notification note')

    @api.onchange('check_in', 'check_out')
    def onchange_dates(self):
        for rec in self:
            if rec.check_in and rec.check_out and rec.error_attendances:
                rec.error_attendances = False
