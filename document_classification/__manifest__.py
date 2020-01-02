# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Document Classification",
    'version': "12.0.1.0.0",
    'depends': ['mail'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Document',
    'summary': """Document Classification""",
    'description': """
Document Classification
=======================
* This module adding tags and categories in attachments and new "Attachment Category" and "Attachment Tag" in Technical.
    """,

    'data': [
        "security/ir.model.access.csv",
        "views/attachment_view.xml",
        "views/attachment_category_view.xml",
        "views/attachment_tag_view.xml",
    ],
}
