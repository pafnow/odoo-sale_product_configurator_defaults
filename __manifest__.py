# Copyright 2020 Pafnow
{
    'name': 'Sale Product Configurator Default Values',
    'version': '13.0.1.0.0',
    'depends': ['sale_product_configurator', 'product_attribute_defaults'],
    'author': 'Pafnow',
    'category': 'Hidden',
    'description': 'Handle default values for attributes of product via the configurator',
    'data': [
        'views/assets.xml',
        'wizard/sale_product_configurator.xml',
    ],
    'installable': True,
    'application': False,
}
