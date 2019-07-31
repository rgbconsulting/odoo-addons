# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Invoice Legal Note",
    'version': "12.0.0.0.0",
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Invoicing Management',
    'summary': """Invoice Legal Note""",
    'description': """
Invoice Legal Note
==================
* Add invoice legal note.
    """,

    'data': [
        'views/res_company_view.xml',
        'views/templates.xml',
    ],
}
