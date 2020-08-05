# Copyright 2020 Pafnow
{
    'name': 'Sale Product Configurator Default Values',
    'version': '13.0.1.0.0',
    'depends': ['sale_product_configurator'],
    'author': 'Pafnow',
    'category': 'Hidden',
    'description': 'Handle default values for attributes of product via the configurator',
    'data': [
        'views/assets.xml',
        'views/partner_view.xml',
        'wizard/sale_product_configurator.xml',
    ],
    'installable': True,
    'application': False,
}
