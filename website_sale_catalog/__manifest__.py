# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Website Sale Catalog',
    'summary': 'Adds catalog in website catalog',
    'version': '12.0.1.0.0',
    'category': 'Website',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting',
    'license': 'AGPL-3',
    'depends': ['website_sale'],
    'description': """
Website Sale Catalog
====================
* This module allows you to create catalogs for displaying groups of products easily in your Website.
    """,

    'data': [
        'security/website_catalog_security.xml',
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/website_catalog_view.xml',
        'views/res_config_settings_view.xml',
        'views/res_partner_view.xml'
    ],
}
