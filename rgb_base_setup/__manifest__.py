# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
		# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'RGB Base Setup',
    'summary': 'Default base modules',
    'category': 'RGB',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'depends': ['contacts',
                'note',
                'calendar',
                'document',
                # server-ux
                'mass_editing',
                'base_technical_features',
                # server-auth
                # 17-06-09 optional : 'password_security',
                #server-brand
                'disable_odoo_online',
                # web
                'web_dialog_size',
                'web_searchbar_full_width',
                'web_responsive',
                #29-4-19 [NOT APROVED]'web_search_with_and',
                # partner-contact
                'base_location_geonames_import',
    ],
    'description': """
RGB Base Setup
==============

* Installs the base modules for a basic setup.
""",

    "installable": True,

}
