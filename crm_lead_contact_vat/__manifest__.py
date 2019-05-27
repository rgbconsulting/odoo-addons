# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Lead Contact VAT",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "",
    "website": "https://www.rgbconsulting.com",
    "author": "RGB Consulting SL",
    "license": "AGPL-3",
    "depends": [
        "crm",
        "account_accountant",
    ],
    'description': """
Lead Contact VAT
==================
* This module adds vat as a new field for leads. 

        """,

    "data": [
        'views/crm_vat.xml',
    ],

    "installable": True,
}
