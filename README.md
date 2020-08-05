# odoo-sale_product_configurator_defaults
Odoo module to handle default values for attributes in the product configurator

This module will add a field on the res.partner to list the attribute values to be used as default for this customer when opening the sale_product_configurator widget.

### Improvments
- Limit default_product_attribute_value_ids on res.partner for one of each attribute type<br>
Example: do not allow to select both Size S and Size M in default_product_attribute_value_ids
- Add default values on product.template
