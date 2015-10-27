#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-rby.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-rby.png'])
    ]


setup(
    name="Electrum-RBY",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'tlslite',
        'dnspython',
    ],
    package_dir={
        'electrum_rby': 'lib',
        'electrum_rby_gui': 'gui',
        'electrum_rby_plugins': 'plugins',
    },
    packages=['electrum_rby','electrum_rby_gui','electrum_rby_gui.qt','electrum_rby_plugins'],
    package_data={
        'electrum_rby': [
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_rby_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-rby'],
    data_files=data_files,
    description="Lightweight RubyCoin Wallet",
    author="rbyDEV",
    author_email="rbycoin@twitter",
    license="GNU GPLv3",
    url="http://electrum-rby.net",
    long_description="""Lightweight RubyCoin Wallet"""
)
