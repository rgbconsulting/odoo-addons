# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def _refund_cleanup_lines(self, lines):
        # BP saas-12.3
        """ This override will link Sale line to all its invoice lines (direct invoice, refund create from invoice, ...)
            in order to have the invoiced quantity taking invoice (in/out) into account in its computation everytime,
            whatever the refund policy (create, cancel or modify).
        """
        result = super(AccountInvoice, self)._refund_cleanup_lines(lines)
        if lines._name == 'account.invoice.line':  # avoid side effects as lines can be taxes ....
            for i, line in enumerate(lines):
                for name, field in line._fields.items():
                    if name == 'sale_line_ids':
                        result[i][2][name] = [(4, line_id) for line_id in line[name].ids]
        return result
