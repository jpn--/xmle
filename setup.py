"""
an extension to xml.etree.ElementTree.Element to handle xml snippets
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='xmle',
	version='0.1',

	description='an extension to xml.etree.ElementTree.Element to handle xml snippets',
	long_description=long_description,

	# The project's main homepage.
	url='https://github.com/jpn--/xmle',

	# Author details
	author='Jeffrey Newman',
	author_email='jnewman@camsys.com',

	# Choose your license
	license='MIT',

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],

	# What does your project relate to?
	keywords='xml xhtml',

	# You can just specify the packages manually here if your project is
	# simple. Or you can use find_packages().
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),

	# List run-time dependencies here.  These will be installed by pip when
	# your project is installed. For an analysis of "install_requires" vs pip's
	# requirements files see:
	# https://packaging.python.org/en/latest/requirements.html

	install_requires=[
		'pandas',
		'cloudpickle',
	],

)