# Copyright 2022 Camptocamp SA (https://www.camptocamp.com).
# @author Iván Todorovich <ivan.todorovich@camptocamp.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    commitment_date = fields.Datetime(readonly=True)

    def _select_sale(self, fields=None):
        res = super()._select_sale(fields=fields)
        res += ", s.commitment_date"
        return res

    def _group_by_sale(self, groupby=""):
        res = super()._group_by_sale(groupby=groupby)
        res += ", s.commitment_date"
        return res
