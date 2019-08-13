# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from odoo import fields, models, api


class BankStatementCloseWarning(models.TransientModel):
    _name = 'account.bank_statement_close_warning'

    name = fields.Char(readonly=True)
    statement = fields.Many2one(comodel_name='account.bank.statement', string='ID', readonly=True)
    line_count = fields.Integer(readonly=True)
    wizard_lines_ids = fields.One2many(comodel_name='account.bank_statement_close_warning_list',
                                       inverse_name='wizard_id')

    @api.one
    def force_close(self):
        for line in self.wizard_lines_ids:
            line.statement_line.active = False
        total = 0.0
        for line in self.statement.line_ids:
            total += line.amount
        if self.statement.balance_end_close == 0:
            self.statement.balance_end_close = self.statement.balance_end_real
        self.statement.balance_end_real = self.statement.balance_start + total
        self.statement.write({'balance_start': self.statement.balance_start})
        self.statement.oper_desact()
        self.statement.button_confirm_bank()


class BankStatementCloseWarningList(models.TransientModel):
    _name = 'account.bank_statement_close_warning_list'

    statement_line = fields.Many2one(comodel_name='account.bank.statement.line')
    wizard_id = fields.Many2one('account.bank_statement_close_warning', ondelete='cascade', readonly=True)
    date = fields.Date()
    name = fields.Char()
    partner_id = fields.Many2one(comodel_name='res.partner')
    ref = fields.Char()
    amount = fields.Float()
    bank_account_id = fields.Many2one(comodel_name='res.partner.bank')
