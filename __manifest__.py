# -*- coding: utf-8 -*-
{
    'name': "parqueatracciones",

    'summary': """
        Gestión de un parque de atracciones""",

    'description': """
        Con este modulo podrá gestionar y organizar su parque de atracciones controlando tanto 
        a sus empleados como a sus clientes
    """,

    'author': "Alejandro Rodriguez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}