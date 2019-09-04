# Copyright 2019 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Tax groups in sale report lines",
    'summary': "Show tax groups in sales report lines",
    'version': '12.0.1.0.0',
    'category': 'Sale Management',
    'website': "https://rgbconsulting.com",
    'author': "RGB Consulting",
    'license': 'AGPL-3',
    'installable': True,
    'depends': ['sale'],
    'data': [
        'views/report_saleorder.xml',
    ],
}
