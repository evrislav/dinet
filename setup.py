import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='dinet',
      version='0.1',
      description='Python interactive console app for generating docker compose structure',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/evrislav/dinet',
      author='Evrislav',
      author_email='evrislav@gmail.com',
      license='MIT',
      packages=['dinet'],
      zip_safe=False)