from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    margin_perc = fields.Float(
        help="Percentage of margin."
    )
