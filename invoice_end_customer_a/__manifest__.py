# -*- coding: utf-8 -*-
{
    'name': 'Invoice End Customer A',
    'version': '16.0.1.1.0',
    'category': 'Account',
    'company': 'Test',
    'author': 'Test',
    'price' : '0.06',
    'currency' : 'USD',
    'website': "",
    'description': """
        -Invoice end customer A.
    """,
    'depends': ['base','account'],
    'data': [
        'views/account_move_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
