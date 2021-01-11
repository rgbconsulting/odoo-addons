# Copyright 2021 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'RGB Base Spanish Localization',
    'summary': 'Base Spanish localization modules',
    'version': '14.0.1.0.0',
    'category': 'RGB',
    'website': 'https://www.rgbconsulting.com',
    'author': 'RGB Consulting SL',
    'license': 'AGPL-3',
    'depends': [
                    'rgb_base_account',
                    'l10n_es',
                # l10n-spain
                    # 'l10n_es_toponyms',
                    'l10n_es_partner',
                    # 'l10n_es_mis_report',
                    # 'l10n_es_account_invoice_sequence',
                    'l10n_es_partner_mercantil',
                    # 'l10n_es_account_bank_statement_import_n43'
    ],
    'description': """
RGB Base Spanish Localization
=============================
* Installs the base spanish localization modules.

    """,
    'installable': True,
}
