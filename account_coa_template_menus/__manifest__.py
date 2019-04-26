# -*- coding: utf-8 -*-
##############################################################################
#
#   Account COA Template Menus
#   Copyright 2018 RGB Consulting, SL
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
    'name': "Account COA Template Menus",
    'version': '10.0.1.0.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Accounting',
    'summary': """Menus for COA templates""",
    'description': """
Account COA Template Menus
==========================
This module adds menus for Chart of Accounts templates.
    """,

    'data': [
        'views/coa_menuitems.xml',
    ],
}
