from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    on_list = fields.Boolean()
