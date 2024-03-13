# -*- coding: utf-8 -*-
# Copyright (C) 2023-Today RGB Informàtica i Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)
{
    'name': "Backup logs",
    'version': '1.0.1',
    'category': 'Tools',
    'summary': """
        Gets backup logs for the current instance
        """,
    'author': 'RGB Informàtica i Consulting SL',
    'website': "https://www.rgbconsulting.com",
    'license': 'AGPL-3',
    'depends': ['base'],

    'description': """
        Gets backup logs for the current instance
    """,

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        "data/ir_cron.xml",
        'views/backup_log_type_views.xml',
        'views/backup_log_record_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
