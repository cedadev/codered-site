#!/usr/bin/env python3

import os, re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    import codered_site.__version__ as version
except ImportError:
    # If we get an import error, find the version string manually
    version = "unknown"
    with open(os.path.join(here, 'codered_site', '__init__.py')) as f:
        for line in f:
            match = re.search('__version__ *= *[\'"](?P<version>.+)[\'"]', line)
            if match:
                version = match.group('version')
                break

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

if __name__ == "__main__":

    setup(
        name = 'codered-site',
        version = version,
        description = 'App theme providing website based on coderedcms',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author = 'Matt Pritchard',
        author_email = 'matt.prithard@stfc.ac.uk',
        url = 'https://github.com/cedadev/codered-site',
        keywords = 'web django bootstrap coderedcms',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = ['coderedcms',],
        #extras_require = { },
    )
