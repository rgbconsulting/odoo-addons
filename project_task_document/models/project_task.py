# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for task in self:
            task.doc_count = Attachment.search_count([('res_model', '=', 'project.task'), ('res_id', 'in', task.ids)])

    def attachment_tree_view(self):
        self.ensure_one()
        domain = [('res_model', '=', 'project.task'), ('res_id', 'in', self.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="o_view_nocontent_smiling_face">
                        Documents are attached to the task</p><p>
                        Send messages or log internal notes with attachments to link
                        documents to your task.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")
