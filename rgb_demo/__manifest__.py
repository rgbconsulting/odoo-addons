# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'RGB Demo',
    'summary': 'Default addons for a basic demo erp',
    'version': '12.0.1.0.0',
    'category': 'RGB',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
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
                'hr_expense'
    ],
    'description': """
RGB Demo
========
* Installs the default modules for a basic demo erp.

    """,

    'demo': [
        'views/demo_user.xml',
    ],

    'installable': True,

}
