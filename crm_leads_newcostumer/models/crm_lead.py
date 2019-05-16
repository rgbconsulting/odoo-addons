# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def create_partner_assignation(self):
        for lead in self:
            context = self._context.copy()
            context.update({'active_model': 'crm.lead', 'active_id': lead.id})
            partner_id = self.env['crm.partner.binding'].with_context(context)._find_matching_partner()
            if not partner_id:
                lead.handle_partner_assignation('create', partner_id)
            else:
                lead.handle_partner_assignation('exist', partner_id)
        return True
