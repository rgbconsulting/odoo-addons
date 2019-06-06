# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Purchase Notes Html",
    'version': "12.0.0.0.0",
    'depends': ['hr', 'purchase'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Purchase Notes Html',
    'summary': """Purchase Notes Html""",
    'description': """
Purchase Notes Html
===================
* This module change "Notes" field type "Text" for "Html". 
    """,

    'data': [
        'views/purchase_view.xml',
    ],
}