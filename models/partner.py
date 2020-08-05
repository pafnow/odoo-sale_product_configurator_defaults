# Copyright 2020 Pafnow

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    default_product_attribute_value_ids = fields.Many2many('product.attribute.value')
