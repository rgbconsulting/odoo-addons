# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    _description = 'Purchase Order'

    notes = fields.Html('Terms and Conditions')
