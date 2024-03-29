# -*- coding: utf-8 -*-
{
    'name': "cnam_hr_payroll",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_payroll', 'mg_payroll_core'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/omsi_periodic_declaration.xml',
        'wizard/osief_periodic_declaration.xml',
        'data/hr_payroll_data.xml',
        'views/report_payslip_standard.xml',
        'views/views.xml',
        'views/irsa_wizard_view.xml',
        'views/solde.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
