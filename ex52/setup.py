#!/usr/bin/env python

try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

setup(description='Learn Python then Hard Way - Ex 52',
    author='Gabriel Ionescu',
    url='',
    download_url='',
    author_email='ionescuig@yahoo.com',
    version='1.0',
    install_requires=['nose'],
    packages=['ex52'],
    scripts=[],
    name='ex52'
    )