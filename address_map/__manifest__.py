{
    'name': 'Address Map Static',
    'version': '1.0.1',
    'summary': 'Adds static map display for partner addresses using OpenStreetMap',
    'category': 'Tools',
    'author': 'J.Boehm',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'installable': True,
    'application': False,
}
