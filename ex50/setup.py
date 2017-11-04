try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description': 'lpthw ex50',
    'author': 'Gabriel Ionescu',
    'url': '',
    'download_url': '',
    'author_email': 'ionescuig@yahoo.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
