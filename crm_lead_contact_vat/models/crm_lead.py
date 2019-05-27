# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models, fields, api, tools


class Lead(models.Model):
    _inherit = 'crm.lead'

    vat = fields.Char(string="Tax ID")

    @api.multi
    def write(self, vals):
        if vals.get('vat'):
            contact_name = (vals.get('contact_name') or self.contact_name)
            if not contact_name:
                contact_name = 'Test vat'
            country = vals.get('country_id') or (self.country_id and self.country_id.id)
            if not country:
                country = self.env.ref('base.es').id
            res = self.env['res.partner'].new(
                {'name': contact_name, 'vat': vals.get('vat'), 'country_id': country})
            res.check_vat()
        return super(Lead, self).write(vals)

    # FIXME - is there a way to avoid override ?
    @api.multi
    def _lead_create_contact(self, name, is_company, parent_id=False):
        email_split = tools.email_split(self.email_from)
        values = {
            'name': name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'comment': self.description,
            'team_id': self.team_id.id,
            'parent_id': parent_id,
            'phone': self.phone,
            'mobile': self.mobile,
            'email': email_split[0] if email_split else False,
            'fax': self.fax,
            'title': self.title.id,
            'function': self.function,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'is_company': is_company,
            'type': 'contact',
            'vat': self.vat
        }
        return self.env['res.partner'].create(values)

    @api.multi
    def create(self, vals):
        if vals.get('vat'):
            contact_name = vals.get('contact_name', 'Test vat')
            country = vals.get('country_id')
            if not country:
                country = self.env.ref('base.es').id
            res = self.env['res.partner'].new(
                {'name': contact_name, 'vat': vals.get('vat'), 'country_id': country})
            res.check_vat()
        return super(Lead, self).create(vals)
