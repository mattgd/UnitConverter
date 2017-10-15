import os
import re

from setuptools import setup
from setuptools import find_packages
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

def readme():
    with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
        return f.read()

def version():
    with open(os.path.join(here, 'UnitConverter', '__init__.py')) as v_file:
        return re.compile(r".*__version__ = '(.*?)'",
                          re.S).match(v_file.read()).group(1)

install_requires = [
    'requests'
]

tests_require = [
    'nose',
]

scripts = [
    'bin/unit_converter'
]

setup(name='UnitConverter',
      version=version(),
      description='"Unit conversion helper"',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Environment :: Console'
      ],
      keywords='Unit Conversion',
      author='Matt Dzwonczyk',
      author_email='hello@mattdzwonczyk.com ',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=install_requires,
      test_suite='nose.collector',
      tests_require=tests_require,
      include_package_data=True,
      zip_safe=False,
      scripts=scripts)

