# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WebsiteCatalog(models.Model):
    _name = 'website.catalog'

    name = fields.Char(required=True)
    description = fields.Text()
    product_ids = fields.Many2many(comodel_name='product.template', string='Products')
    category_ids = fields.Many2many(comodel_name='product.public.category', string='Categories')
    partner_ids = fields.One2many(comodel_name='res.partner', inverse_name='catalog_id', string='Customers')
    customers_count = fields.Integer(compute='_count_customer_ids', readonly=True)

    @api.multi
    @api.depends('partner_ids')
    def _count_customer_ids(self):
        for rec in self:
            rec.customers_count = len(rec.partner_ids)

    @api.multi
    def _get_domain(self):
        domain = []
        if self.product_ids.ids:
            domain.append(('id', 'in', self.product_ids.ids))
        if self.category_ids.ids:
            if self.product_ids.ids:
                domain = ['|'] + domain
            domain.append(('public_categ_ids', 'child_of', self.category_ids.ids))
        return domain

    @api.multi
    def action_view_customers(self):
        self.ensure_one()
        return {
            'name': _('Customers'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'domain': [('catalog_id', 'in', self.ids)],
        }
