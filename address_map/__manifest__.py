{
    'name': 'Address Map Static',
    'version': '1.0',
    'summary': 'Affiche une carte statique pour une adresse ou coordonnées GPS',
    'category': 'Tools',
    'author': 'Votre Nom',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'installable': True,
    'application': False,
}
