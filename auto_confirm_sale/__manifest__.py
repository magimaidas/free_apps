{
    'name': 'Auto Sale Confirm',
    'description': 'Automatically confirm sale order which is in draft, periodically by scheduled actions',
    'version': '12.0.0',
    'license': 'LGPL-3',
    'author': 'Magimaidas',
    'website': 'https://www.linkedin.com/in/magimaidas/',
    'depends': [
        'sale_management',
        'sale',
    ],
    'data': [
        'data/scheduled_action.xml',
    ],
    'application': True,
    'installable': True,
}
