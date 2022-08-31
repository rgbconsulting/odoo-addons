# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_validation_fail = fields.Boolean(string='VAT Validation Fail', readonly=True, default=False)

    @api.constrains('vat')
    def check_vat(self):
        if self.env.context.get('company_id'):
            company = self.env['res.company'].browse(self.env.context['company_id'])
        else:
            company = self.env.user.company_id
        if company.disable_vat_check:
            for partner in self:
                try:
                    super(ResPartner, partner).check_vat()
                    if partner.vat_validation_fail:
                        partner.write({'vat_validation_fail': False})
                except:
                    if not partner.vat_validation_fail:
                        partner.write({'vat_validation_fail': True})
        else:
            super(ResPartner, self).check_vat()
            if any(rec.vat_validation_fail for rec in self):
                self.write({'vat_validation_fail': False})
