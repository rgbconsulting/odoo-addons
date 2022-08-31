# Copyright 2022 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'VAT fix translate',
    'version': '12.0.1.0.0',
    'category': 'Accounting/Accounting',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting',
    'license': 'AGPL-3',
    'depends': ['base_vat'],
    'description': """
This module fix wrong translation
    """,

    'data': [
        'views/res_partner_views.xml',
    ],
}
