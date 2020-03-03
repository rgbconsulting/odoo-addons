# -*- coding: utf-8 -*-
# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Website Sale Popup Variants",
    "summary": "Adds Variants in the popup when Purchasing in the Website",
    "version": "10.0.1.0.0",
    "category": "Website",
    "website": "https://www.rgbconsulting.com",
    "author": "RGB Consulting",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "website_sale_options",
    ],
    'description': """
Website Sale Popup Variants
==========================
Adds the variants of the product in the popup when purchasing in the Website.
        """,
    "data": [
        'templates/website_sale_add_to_cart_template.xml',
    ],
}
