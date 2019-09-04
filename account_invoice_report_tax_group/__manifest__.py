# Copyright 2019 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Tax groups in invoice report lines",
    'summary': "Show tax groups in invoice report lines",
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'website': "https://rgbconsulting.com",
    'author': "RGB Consulting",
    'license': 'AGPL-3',
    'depends': ['sale'],
    'installable': True,
    'data': [
        'views/report_invoice.xml',
    ],
}
