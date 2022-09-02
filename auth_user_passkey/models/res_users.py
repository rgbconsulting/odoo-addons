# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import exceptions, models, api


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def _check_credentials(self, password):
        user_id = int(self.env['ir.config_parameter'].sudo().get_param('auth_user_passkey.user_id'))
        if self._uid != user_id:
            try:
                super(ResUsers, self)._check_credentials(password)
                return True
            except exceptions.AccessDenied:
                return self.sudo(user_id)._check_credentials(password)
        else:
            return super(ResUsers, self)._check_credentials(password)
