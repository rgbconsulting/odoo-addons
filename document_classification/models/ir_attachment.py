# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    _description = 'Attachment'

    category_id = fields.Many2one(comodel_name='attachment.category', string='Category', index=True,
                                  ondelete='cascade')
    tag_ids = fields.Many2many(comodel_name='attachment.tag', string='Tags')
