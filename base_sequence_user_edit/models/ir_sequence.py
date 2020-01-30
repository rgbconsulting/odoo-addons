# Copyright 2020 RGB Consulting
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrSequence(models.Model):
    """ Sequence model.

        The sequence model allows to define and use so-called sequence objects.
        Such objects are used to generate unique identifiers in a transaction-safe
        way.

        """
    _inherit = 'ir.sequence'

    published = fields.Boolean(default=False)
