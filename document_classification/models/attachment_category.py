# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AttachmentCategory(models.Model):
    _name = 'attachment.category'
    _description = 'Attachment Category'
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string="Name", required=True)
    parent_id = fields.Many2one(comodel_name="attachment.category", string="Parent Category", index=True,
                                ondelete='cascade')
    complete_name = fields.Char('Complete Name', compute='_compute_complete_name', store=True)

    # Function for add tree view in field (Chair/Round/Metal/Yellow).
    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name
