# -*- coding: utf-8 -*-

{
    "name" : "POS Kitchen Receipt Print",
    "version" : ".1.0",
    'category': 'Point Of Sale',
    'author': 'Zero Systems',
    'company': 'Zero for Information Systems',
    'website': "https://www.erpzero.com",
    'email': "sales@erpzero.com",
    "images":["logo.PNG"],
    'summary': 'POS Kitchen Receipt Print without IOT box.',
    "description": """ This app use to print the receipt for kitchen order. only non-printed 
    or newly added product will be printed for the same order for restricting the duplication. 
    
    POS Kitchen Receipt Print
    Kitchen Receipt Print
    print receipt 
    print pos kictchen receipt
    kitchen receipt 
    Print POS Kitchen Receipt
    point of sale kitchen receipt
    POS Kitchen Order Notes
    POS Restaurant note
    POS Restaurant order note
    Restaurant kitchen receipt
    pos receipt kitchen order receipt
    kitchen order receipt
    kitchen notes
    


     """,
    "depends" : ['base','point_of_sale','pos_restaurant'],
    "data": [
        'views/custom_js_added.xml',
        'views/pos_config_inherit.xml',
    ],
    'qweb': [
    'static/src/xml/pos.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    
}
