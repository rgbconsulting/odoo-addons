# Copyright 2022 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Disable VAT Check',
    'summary': 'Disable VAT validation for company',
    'version': '14.0.1.0.0',
    'category': 'base',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'depends': ['base_vat'],
    'description': """
Disable Vat Check
=================
*   This module allows disabling VAT validation by company.
*   The module marks the contacts with incorrect VAT for easy identification.
    """,

    'data': [
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
    ],
}
