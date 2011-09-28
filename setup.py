import os
import sys
from distutils.core import setup
from django.core.management.commands.compilemessages import compile_messages


license_text = open('LICENSE.txt').read()
long_description = open('README.rst').read()


setup(
    name = 'templated-emails',
    version = "0.4",
    url = 'https://github.com/philippWassibauer/templated-emails',
    author = "Philipp Wassibauer",
    author_email = "phil@gidsy.com",
    license = license_text,
    packages = ['templated_emails'],
    data_files=[('', ['LICENSE.txt', 'README.rst'])],
    description = 'Like django-notifications, but just for sending plain emails. Written because it is ennoying to fork other apps just to make an email into an HTML email',
    long_description=long_description,
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content'],
    install_requires=[
        'pynliner',
        'cssutils',
    ],
)
