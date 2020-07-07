# -*- coding: utf-8 -*-
# Copyright 2020 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'RGB Base Setup',
    'summary': 'Default base modules',
    'category': 'RGB',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'version': '13.0.1.0.0',
    'depends': ['contacts',
                'note',
                'calendar',
                'attachment_indexation',
                # server-ux
                'mass_editing',
                'base_technical_features',
                # server-auth
                # 17-06-09 [optional] : 'password_security',
                # server-brand
                'disable_odoo_online',
                # web
                'web_dialog_size',
                'web_no_bubble',
                'web_responsive',
                #'web_widget_many2many_tags_multi_selection',
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
