# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Base Sequence User Edit',
    'summary': 'Base Sequence User Edit',
    'version': '12.0.1.0.1',
    'category': 'Usability',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting SL',
    'license': 'AGPL-3',
    'description': """
Base Sequence User Edit
=======================
This module implements new sequence submenu for base users.
    """,
    'depends': [
        'account'
    ],
    'data': [
        'security/base_sequence_user_edit_security.xml',
        'security/ir.model.access.csv',
        'views/base_sequence_user_edit_views.xml',
    ],
    'installable': False,
}
