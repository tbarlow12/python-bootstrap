from setuptools import setup, find_packages

setup(name='example_package',
      version='0.0.1',
      description='Python Bootstrap Project',
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
