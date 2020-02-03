# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_move_create(self):
        """ Creates invoice related analytics and financial move lines """
        self.filtered(lambda s: not s.date and s.type in ('in_invoice', 'in_refund')).write(
            {'date': fields.Date.context_today(self)})
        return super(AccountInvoice, self).action_move_create()
