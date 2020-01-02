# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AttachmentTag(models.Model):
    _name = 'attachment.tag'
    _description = 'Attachment Tag'

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string='Color Index')
