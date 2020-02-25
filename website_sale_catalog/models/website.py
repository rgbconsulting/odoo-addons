# -*- coding: utf-8 -*-
# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'

    catalog_id = fields.Many2one(comodel_name='website.catalog', string='Catalog')

    @api.multi
    def sale_product_domain(self):
        res = super(Website, self).sale_product_domain()
        catalog = self.env.user.partner_id.catalog_id or self.catalog_id
        if catalog:
            res.extend(catalog._get_domain())
        return res
