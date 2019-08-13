# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.
{
    'name': "Bank statment close",
    'version': '10.0.0.1.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Account',
    'summary': """Bank statment close""",
    'description': """
Bank statment close
===================
* This module allows to deactivate the irreconcilable bank statement lines (i.e. bank lines related to SEPA payment 
returns), allowing to close the extract. It also allows to undo it by activating again the deactivated lines.
    """,

    'data': [
        'views/account_bank_statement.xml',
        'wizard/account_bank_statement_close_warning.xml',
    ]
}