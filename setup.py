from setuptools import setup, find_packages
from io import open
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(name='example_package',
      version=__version__,
      description='Python Bootstrap Project',
      long_description=read('README.md'),
      url='https://github.com/tbarlow12/python-bootstrap',
      author='Your Name',
      author_email='your.email@url.com',
      license='MIT',
      packages=find_packages(),
      # Anything your package depends on
      install_requires=[
          'flask',
          'numpy'
      ])
