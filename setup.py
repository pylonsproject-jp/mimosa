from setuptools import setup, find_packages
import os

__version__ = '0.0'
__author__ = 'pylonsproject.jp'

requires = [
    "pyramid",
    "pyramid_tm",
    "pyramid_layout",
    "sqlalchemy",
    "zope.sqlalchemy",
    "deform",
    "colander",
    "deform_bootstrap",
]

tests_require = [
]

here = os.path.dirname(__file__)

def _read(name):
    try:
        with open(name) as f:
            return f.read()
    except IOError:
        return ""

readme = _read(os.path.join(here, 'README.rst'))
changes = _read(os.path.join(here, 'CHANGES.txt'))
contrib = _read(os.path.join(here, 'CONTRIBUTORS.txt'))

setup(name="mimosa",
      version=__version__,
      author=__author__,
      description="administrator interface for sqlalchemy with pyramid.",
      long_description=readme+"\n"+changes+"\n"+contrib,
      packages=find_packages(exclude=['tests', 'demo']),
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          "testing": tests_require,
      },
)
