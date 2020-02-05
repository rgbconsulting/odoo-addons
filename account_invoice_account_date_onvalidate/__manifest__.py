# -*- coding: utf-8 -*-
# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Account Invoice Account Date On Validate',
    'summary': 'Account invoice account_date onvalidate',
    'version': '10.0.1.0.0',
    'category': 'Accounting & Finance',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting SL',
    'license': 'AGPL-3',
    'description': """
Account Invoice Account_date on Validate
========================================
* This module improves accounting date field in purchase (refund included) invoices
filling it with the date of validation if left blank.
    """,
    'depends': [
        'account'
    ],
}
