# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Project Task Document",
    'summary': "Shows Project Task Document",
    'version': "12.0.1.0.0",
    'category': 'Project',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'depends': [
        'project',
        'document',
    ],
    'description': """
Project Task Document
=====================
* This module adds button in tasks for viewing documents attached
    """,
    'data': [
        "views/project_task_view.xml",
    ],
}
