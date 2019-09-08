#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='git_stamp',
    version='0.0.1',
    scripts=[ 'bin/timestamp' ],
    install_requires=[ 'dulwich' ],
    provides=[ 'git_stamp' ],
    author='Justin Menga',
    author_email='justin.menga@gmail.com',
    url='https://github.com/mixja/git-stamp',
    description='Command-line utility for resetting file system timestamps based upon Git timestamps',
    keywords='git timestamp',
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
)