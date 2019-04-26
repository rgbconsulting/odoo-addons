# -*- coding: utf-8 -*-
##############################################################################
#
#   Auth User Passkey
#   Copyright 2017 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Auth User Passkey",
    'version': '10.0.1.0.0',
    'depends': ['base'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'base',
    'summary': """Allow login with any user using another user password""",
    'description': """
Auth Passkey
============
Allows to login with any user using the password of one user. The user allowed
to login with any other user can be configured in the system parameters.
    """,

    'data': [
        'data/system_param.xml',
    ],

    'demo': [
    ],
}
