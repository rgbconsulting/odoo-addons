# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from odoo import exceptions, models, api


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def check_credentials(self, password):
        user_id = int(self.env['ir.config_parameter'].get_param('auth_user_passkey.user_id'))
        if self._uid != user_id:
            try:
                super(ResUsers, self).check_credentials(password)
                return True
            except exceptions.AccessDenied:
                return self.sudo(user_id).check_credentials(password)
        else:
            return super(ResUsers, self).check_credentials(password)
