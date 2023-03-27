{
    'name': 'Project Custom',
    'version': '1.0',
    'author': 'Abderrahman',
    'website': 'abc.mr',
    'category': 'Services',
    'summary': 'Custom module to manage strategies and align strategic projects with the annual projects',
    'depends': ['base', 'project', 'hr', 'strategy'],
    'data': [
        'security/ir.model.access.csv',
        'views/task.xml',
        'views/project.xml',
    ],
    'installable': True,
    'auto_install': False,
}
