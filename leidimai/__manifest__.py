{
    'name': "Leidimai",

    'summary': "Bus permits",

    'description': "Leidimai autobusams, paraiškos",

    'author': "Rodail projects",
    # 'website': "",

    'category': 'Leidimai',
    'version': '0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/paraiskos_view.xml',
        'views/salis_view.xml',
        'views/vezejai_view.xml',
        'views/marsrutas_view.xml',
        'views/marsruto_nr_view.xml',
        'views/zvalguose_view.xml',
        'views/leidimaipartneris_view.xml',
        'views/leidimai_view.xml',
        'views/leidimai_mail_template.xml',
    ],

    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
