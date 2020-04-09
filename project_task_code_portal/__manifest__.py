# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Project task code portal',
    'version': '12.0.1.0.0',
    'category': 'Project Management',
    'author': 'RGB Consulting',
    'license': 'AGPL-3',
    'description': """
Project task code portal
========================
* This module adds task code in portal task views
    """,
    'depends': [
        'project_task_code',
    ],
    'data': [
        'views/templates.xml',
    ],
}
