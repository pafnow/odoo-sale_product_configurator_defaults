# Copyright 2020 Pafnow

from odoo import api, models, fields

class SaleProductConfigurator(models.TransientModel):
    _inherit = 'sale.product.configurator'

    partner_id = fields.Many2one('res.partner', "Partner", default=lambda self: self.env.context.get('partner_id', False), readonly=True)

    default_combination = fields.Many2many('product.template.attribute.value', string='Default Attribute Values', compute='_compute_default_combination')

    @api.depends('partner_id')
    def _compute_default_combination(self):
        default_product_template_attribute_value_ids = self.product_template_id.valid_product_template_attribute_line_ids.product_template_value_ids.filtered(
            lambda v: v.product_tmpl_id == self.product_template_id and v.product_attribute_value_id in self.partner_id.default_product_attribute_value_ids
        )
        self.default_combination = self.product_template_id._get_closest_possible_combination(default_product_template_attribute_value_ids._origin)
