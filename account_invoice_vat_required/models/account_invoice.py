# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_move_create(self):
        for invoice in self:
            if invoice.type in ('out_invoice', 'out_refund') and not invoice.partner_id.vat:
                raise UserError(_("You are trying to validate an invoice whose customer doesn't have VAT "))
        return super(AccountInvoice, self).action_move_create()
