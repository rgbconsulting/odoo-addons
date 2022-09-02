# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Auth User Passkey',
    'summary': 'Allow login with any user using another user password',
    'version': '12.0.1.0.0',
    'category': 'base',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting SL',
    'license': 'AGPL-3',
    'depends': ['base'],
    'description': """
Auth Passkey
============
*   Allows to login with any user using the password of one user. The user allowed
    to login with any other user can be configured in the system parameters.
    """,

    'data': [
        'data/system_param.xml',
    ],
}
