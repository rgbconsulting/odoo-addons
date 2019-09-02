# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Tax description for sale report",
    'version': '10.0.1.0.0',
    'depends': ['sale'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Sales',
    'summary': """Change tax description in sales report""",
    'description': """
Tax description for sale report
===============================

This module changes tax description in sales report.
""",

    'data': [
        'views/l10n_es_sale_order_report.xml',
    ],
}
