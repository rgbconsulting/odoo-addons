# Copyright 2021 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'RGB Demo Website Installation',
    'summary': 'Default addons for demo website',
    'version': '14.0.1.0.0',
    'category': 'RGB',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'depends': ['rgb_demo',
                'website',
                'website_sale',
                'website_payment',
                'website_crm',
                'website_blog',
                'website_forum',
                'website_event',
                'website_hr_recruitment',
                ],
    'description': """
RGB Demo Website Installation
=============================
* Installs the default modules for a demo website.

    """,

    'demo': [
        'views/demo_user.xml',
    ],

    'installable': True,

}
