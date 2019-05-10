# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    disable_vat_check = fields.Boolean(string='Disable VAT Check', default=False)
