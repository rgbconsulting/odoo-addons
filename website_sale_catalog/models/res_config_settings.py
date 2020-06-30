# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    catalog_id = fields.Many2one(related='website_id.catalog_id', relation='catalog_id', string='Catalog',
                                 readonly=False)
