# -*- coding: utf-8 -*-
# Copyright (C) 2023-Today RGB Informàtica i Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)
{
    'name': "Login logs",
    'version': '0.1',
    'category': 'Tools',
    'summary': """
        Gets de journalctl login logs for the current instance
        """,
    'author': 'RGB Informàtica i Consulting SL',
    'website': "https://www.rgbconsulting.com",
    'license': 'AGPL-3',

    'depends': ['base'],

    'description': """
        Gets de journalctl login logs for the current instance
    """,

    'data': [
        'security/ir.model.access.csv',
        "data/ir_cron.xml",
        'views/login_logs_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
