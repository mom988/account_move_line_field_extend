# -*- coding: utf-8 -*-
{
    'name': "account_move_line_field_extend",

    'summary': """
        account_move_line_field_extend""",

    'description': """
        account_move_line_field_extend
    """,

    'author': "rsh",
    'website': "http://erp.icu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
