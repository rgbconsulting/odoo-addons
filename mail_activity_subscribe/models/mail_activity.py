# -*- coding: utf-8 -*-
# Copyright 2022 RGB Consulting SL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def create(self, values):
        # We make super() of create() method to extend the code
        activity = super().create(values)
        activity_user = activity.sudo(self.env.user)

        # El usuario que planifica una actividad, pasa a seguir las 'Actividades' para el objeto en el que la planifica
        mail_message_subtypes_ids = self.env['mail.message.subtype'].default_subtypes(activity.res_model)[0].ids
        mail_message_subtypes_ids.append(self.env.ref('mail.mt_activities').id)
        self.env[activity_user.res_model].browse(activity_user.res_id).message_subscribe(
            partner_ids=[self.env.user.partner_id.id],
            subtype_ids=mail_message_subtypes_ids)
        return activity
