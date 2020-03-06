# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Picking Description Line',
    'version': '12.0.1.0.0',
    'depends': ['stock'],
    'license': 'AGPL-3',
    'author': 'RGB Consulting',
    'website': 'https://www.rgbconsulting.com',
    'category': 'Warehouse',
    'summary': 'Stock Picking Description Line',
    'description': '''
Stock Picking Description Line
==============================
* This module allows to print moves description in picking reports and add product description in picking
    ''',

    'data': [
        'views/stock_picking_views.xml',
        'views/templates.xml',
    ],
}
