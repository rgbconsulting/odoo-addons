# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Demo
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
    'name': 'RGB Demo',
    'version': '10.0.0.1.0',
    'depends': ['rgb_base_setup',
                'crm',
                'sale',
                'project',
                'hr',
                'stock',
                'purchase',
                'point_of_sale',
                'mrp',
                'fleet',
                'hr_timesheet_sheet',
                'hr_holidays',
                'hr_expense'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'RGB',

    'summary': 'Default addons for a basic demo erp',

    'description': """
RGB Demo
========

Installs the default modules for a basic demo erp.

    """,

    'data': [
    ],

    'demo': [
        'views/demo_user.xml',
    ],
    'installable': True,
    'application': False,
}
