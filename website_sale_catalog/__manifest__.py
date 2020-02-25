# -*- coding: utf-8 -*-
# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Website Sale Catalog",
    "summary": "Adds catalog in website catalog",
    "version": "10.0.1.0.0",
    "category": "Website",
    "website": "https://www.rgbconsulting.com",
    "author": "RGB Consulting",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "website_sale",
    ],
    "data": [
        'security/website_catalog_security.xml',
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/website_catalog_view.xml',
        'views/website_settings_view.xml',
        'views/res_partner_view.xml',
    ],
}
