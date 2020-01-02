# -*- coding: utf-8 -*-
# Copyright 2019 RGB Consulting SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'RGB Base Accounting',
    'summary': 'Installs Base Accounting modules',
    'version': '12.0.1.0.0',
    'category': 'RGB',
    'website': "https://www.rgbconsulting.com",
    'author': "RGB Consulting SL",
    'license': 'AGPL-3',
    'depends': [# account-financial-tools
                    'account_balance_line',
                    'account_renumber',
                    'account_fiscal_position_vat_check',
                    'account_move_line_tax_editable',
                    'account_lock_date_update',
                # account-invoicing
                    'account_invoice_check_total',
                    'account_invoice_refund_link',
                    'account_invoice_tax_required',
                    'account_invoice_supplier_ref_unique',
                    'account_invoice_fiscal_position_update',
                    'account_payment_term_extension',
                # account-payment
                    'account_due_list',
                # account-financial-reporting
                    'account_financial_report',
                    'account_tax_balance',
    ],
    'description': """
RGB Base Accounting
===================
* Installs base accounting modules.

    """,

    'installable': True,

}
