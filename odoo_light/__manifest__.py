# -*- coding: utf-8 -*-
{
        'name': 'Odoo Light',
        'version': '19.0.1.1.3',
        'category': 'Extra Tools',
        'summary': 'Clean and minimal Odoo interface by hiding unnecessary app menus and icons on a per-user basis.',
        'description': """
        Clean and minimal Odoo interface by hiding unnecessary app menus and icons on a per-user basis.""",
        'author': 'u01',
        'company': 'Inventions Technologies',
        'maintainer': 'Inventions Technologies',
        'website': "http://it.co.tz",
        'depends': ['base'],
        'data': [
            'views/res_users_views.xml',
            'views/ir_ui_menu_views.xml',
            ],
        'images': ['static/description/icon.png'],
        'installable': True,
        'auto_install': False,
        'application': False,
        }
