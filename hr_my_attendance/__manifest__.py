# Copyright 2020 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Hr My Attendace",
    'version': '12.0.1.0.0',
    'depends': ['hr_attendance'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Human Resources',
    'summary': """Hr My attendance""",
    'description': """
Hr My Attendace
===============

This module implements new menu and with new view in hr attendance.
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/hr_my_attendance_view.xml',
        'views/hr_attendance_view.xml',
    ],
}
