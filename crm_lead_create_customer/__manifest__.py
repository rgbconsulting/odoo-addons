# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Leads New Customer",
    "summary": "Leads New Customer Creation",
    "version": "10.0.1.0.0",
    "category": "",
    "website": "https://www.rgbconsulting.com",
    "author": "RGB Consulting SL",
    "license": "AGPL-3",
    "depends": [
        "crm",
    ],
    'description': """
Leads New Customer
==================
* This module adds a new button for the creation of the new customer from the contact information of the lead.

        """,

    "data": [
        'views/crm_lead.xml',
    ],

    "installable": True,
}
