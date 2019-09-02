# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': "Tax description for invoice report",
    'version': '11.0.1.0.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Sales',
    'summary': """Change tax description in invoices report""",
    'description': """
Tax description for invoice report
==================================

This module changes tax description in invoices report.
""",

    'data': [
        'views/l10n_es_account_invoice_report.xml',
    ],
}
