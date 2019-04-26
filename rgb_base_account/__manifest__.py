# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Base Accounting
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
    'name': 'RGB Base Accounting',
    'version': '10.0.1.0.0',
    'depends': ['account_accountant',
                # account-financial-tools
                  # 'account_balance_line',
                'account_renumber',
                'account_fiscal_position_vat_check',
                'account_invoice_tax_required',
                'account_move_line_payable_receivable_filter',
                'account_move_line_tax_editable',
		'account_lock_date_update',
                # account-invoicing
                'account_invoice_check_total',
                'account_invoice_refund_link',
                'account_group_invoice_line',
                'account_invoice_supplier_ref_unique',
                'account_invoice_fiscal_position_update',
                'account_payment_term_extension',
                #account-payment
                'account_due_list',
                #account-financial-reporting
                'account_financial_report_qweb',
                'account_tax_balance',
                #bank-statement-import
                  #'base_bank_account_number_unique',
                ],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'RGB',

    'summary': 'Installs Base Accounting modules',

    'description': """
RGB Base Accounting
===================


Installs base accounting modules.
    """,

    'data': [
    ],

    'demo': [
    ],
    'installable': True,
    'application': False,
}
