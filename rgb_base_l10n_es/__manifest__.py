# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Base Spanish Localization
#   Copyright 2017 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'RGB Base Spanish Localization',
    'version': '11.0.1.0.0',
    'depends': ['rgb_base_account',
                #10n-spain
                'l10n_es_toponyms',
                'l10n_es_partner',
                'l10n_es_account_invoice_sequence',
                'l10n_es_partner_mercantil',
                'l10n_es_account_bank_statement_import_n43',
		'l10n_es_mis_report',
		# mis-builder
		'mis_builder',
],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'RGB',

    'summary': 'Base Spanish localization modules',

    'description': """
RGB Base Spanish Localization
=============================

Installs the base spanish localization modules.
    """,

    'data': [
    ],

    'demo': [
    ],
    'installable': True,
    'application': False,
}
