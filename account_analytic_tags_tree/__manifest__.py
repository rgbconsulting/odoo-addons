# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.
{
    'name': "Account Analytic Tags Tree",
    'version': '10.0.1.0.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Accounting',
    'summary': """Customizations for account module""",
    'description': """
Account Analytic Tags Tree
==========================

This module adds new field account_tag_ids in tree view.
    """,

    'data': [
        'views/account_analytic_view.xml',
    ],
}
