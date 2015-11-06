#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import os


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
HISTORY = open(os.path.join(here, 'HISTORY.rst')).read()

install_requires = ['rebulk>=0.4.2', 'regex', 'babelfish>=0.5.5', 'python-dateutil']

setup_requires = ['pytest-runner']

tests_require = ['pytest', 'pytest-benchmark', 'PyYAML']

entry_points = {
    'console_scripts': [
        'guessit = guessit.__main__:main'
    ],
}


exec(open("guessit/__version__.py").read())  # load version without importing guessit

args = dict(name='guessit',
            version=__version__,
            description='GuessIt - a library for guessing information from video filenames.',
            long_description=README + '\n\n' + HISTORY,
            # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers=['Development Status :: 3 - Alpha',
                         'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                         'Operating System :: OS Independent',
                         'Intended Audience :: Developers',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.3',
                         'Programming Language :: Python :: 3.4',
                         'Programming Language :: Python :: 3.5',
                         'Topic :: Multimedia',
                         'Topic :: Software Development :: Libraries :: Python Modules'
                         ],
            keywords='python library release parser name filename movies series episodes animes',
            author='Rémi Alvergnat',
            author_email='toilal.dev@gmail.com',
            url='http://guessit.readthedocs.org/',
            download_url='https://pypi.python.org/packages/source/g/guessit/guessit-%s.tar.gz' % __version__,
            license='LGPLv3',
            packages=find_packages(),
            include_package_data=True,
            install_requires=install_requires,
            setup_requires=setup_requires,
            tests_require=tests_require,
            entry_points=entry_points,
            test_suite='guessit.test',
            )

setup(**args)
