# -*- coding: utf-8 -*-
{
    'name': "Active Company Visibility",
    'version': '0.0.1',
    'category': 'Accounting',
    'summary': "Module that allows the company name to always be visible",
    "author": "RGB Informàtica i Consulting S.L.",
    'website': "https://www.rgbconsulting.com/",
    'depends': ['base', 'web'],
    "assets": {
        "web.assets_backend": [
            "active_company_visibility/static/src/js/switch_company_menu_patch.js",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
