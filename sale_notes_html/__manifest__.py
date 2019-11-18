# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Sale Notes Html",
    'version': "12.0.0.0.0",
    'depends': ['hr', 'sale'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Sales',
    'summary': """Sale Notes Html""",
    'description': """
Sale Notes Html
===============
* This module changes "Note" field type "Text" for "Html". 
    """,

    'data': [
        'views/sale_order_view.xml',
    ],
}
