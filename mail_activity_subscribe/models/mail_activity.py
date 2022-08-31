# -*- coding: utf-8 -*-
# Copyright 2022 RGB Consulting SL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, exceptions, _


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def create(self, values):
        # already compute default values to be sure those are computed using the current user
        values_w_defaults = self.default_get(self._fields.keys())
        values_w_defaults.update(values)

        # continue as sudo because activities are somewhat protected
        activity = super(MailActivity, self.sudo()).create(values_w_defaults)
        activity_user = activity.sudo(self.env.user)
        activity_user._check_access('create')
        need_sudo = False
        try:  # in multicompany, reading the partner might break
            partner_id = activity_user.user_id.partner_id.id
        except exceptions.AccessError:
            need_sudo = True
            partner_id = activity_user.user_id.sudo().partner_id.id

        # send a notification to assigned user; in case of manually done activity also check
        # target has rights on document otherwise we prevent its creation. Automated activities
        # are checked since they are integrated into business flows that should not crash.
        if activity_user.user_id != self.env.user:
            if not activity_user.automated:
                activity_user._check_access_assignation()
            if not self.env.context.get('mail_activity_quick_update', False):
                if need_sudo:
                    activity_user.sudo().action_notify()
                else:
                    activity_user.action_notify()

        self.env[activity_user.res_model].browse(activity_user.res_id).message_subscribe(partner_ids=[partner_id])
        # El usuario que planifica una actividad, pasa a seguir las 'Actividades' para el objeto en el que la planifica
        mail_message_subtypes_ids = self.env['mail.message.subtype'].default_subtypes(activity.res_model)[0].ids
        mail_message_subtypes_ids.append(self.env.ref('mail.mt_activities').id)
        self.env[activity_user.res_model].browse(activity_user.res_id).message_subscribe(
            partner_ids=[self.env.user.partner_id.id],
            subtype_ids=mail_message_subtypes_ids)
        if activity.date_deadline <= fields.Date.today():
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'res.partner', activity.user_id.partner_id.id),
                {'type': 'activity_updated', 'activity_created': True})
        return activity_user
