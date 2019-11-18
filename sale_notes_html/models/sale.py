# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _default_note(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'sale.use_sale_note') and self.env.user.company_id.sale_note or ''

    note = fields.Html(string='Terms and Conditions', default=_default_note)
