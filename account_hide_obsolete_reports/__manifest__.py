# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Hide Obsolete Reports",
    "summary": "Hides obsolete reports menu in accounting",
    "version": "10.0.1.0.0",
    "category": "Accounting / Reports",
    "website": "https://www.rgbconsulting.com",
    "author": "RGB Consulting SL",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account_accountant",
    ],
    "data": [
        'views/account_menuitem.xml',
    ],
}
