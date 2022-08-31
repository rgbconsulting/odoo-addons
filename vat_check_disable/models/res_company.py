# Copyright 2022 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    disable_vat_check = fields.Boolean(string='Disable VAT Check', default=False)
