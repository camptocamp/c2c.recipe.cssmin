#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'c2c.recipe.cssmin',
    version = '0.6',
    license = 'MIT License',

    author  = 'Frederic Junod',
    author_email = 'frederic.junod@camptocamp.com',
    url = 'https://github.com/camptocamp/c2c.recipe.cssmin',

    description = 'A buildout recipe to merge and compress css files',
    long_description = open('README.rst').read(),

    classifiers = [
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],

    install_requires = ['cssmin'],
    packages = find_packages(),
    namespace_packages = ['c2c', 'c2c.recipe'],
    entry_points = {'zc.buildout' : ['default = c2c.recipe.cssmin.buildout:CssMin']}
)
