# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from odoo import models, api, fields, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import Warning


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement'

    balance_end_close = fields.Monetary(string='Bank Ending Balance', readonly=True)
    op_desact = fields.Float(string="Value of deactivated operations", readonly=True)

    @api.multi
    def oper_desact(self):
        total = 0
        for line in self.env['account.bank.statement.line'].search(
                [['statement_id.id', '=', self.id], ['active', '=', False]]):
            total += line.amount
        self.op_desact = total

    @api.one
    def button_draft(self):
        self.balance_end_real = self.balance_end_close
        self.balance_end_close = 0
        self.op_desact = 0
        for line in self.env['account.bank.statement.line'].search(
                [['statement_id.id', '=', self.id], ['active', '=', False]]):
            line.active = True
        self.write({'balance_start': self.balance_start})  # Trigger balance_enc calc
        self.oper_desact()
        return super(AccountBankStatementLine, self).button_draft()

    @api.multi
    def button_force_close(self):
        lines = []
        wizard_id = False
        for line in self.line_ids:
            if not (line.journal_entry_ids.ids or line.account_id.id):
                lines.append((0, 0, {
                    'date': line.date,
                    'name': line.name,
                    'statement_line': line.id,
                    'ref': line.ref,
                    'partner_id': line.partner_id.id,
                    'bank_account_id': line.bank_account_id.id,
                    'amount': line.amount,
                }))

                wizard_id = self.env['account.bank_statement_close_warning'].create(
                    {'wizard_lines_ids': lines, 'statement': self.id, 'line_count': len(lines)})

        if not wizard_id:
            raise Warning(_("No line to close"))
        else:
            return {
                'name': 'Bank statement force close',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'account.bank_statement_close_warning',
                'res_id': wizard_id.id,
                'type': 'ir.actions.act_window',
                'target': 'new',
            }

    @api.one
    @api.depends('line_ids', 'balance_start', 'line_ids.amount', 'balance_end_real')
    def _end_balance(self):
        self.total_entry_encoding = sum([line.amount for line in self.line_ids.filtered(lambda s: s.active)])
        self.balance_end = self.balance_start + self.total_entry_encoding
        self.difference = self.balance_end_real - self.balance_end
