from setuptools import setup
from os.path import join, dirname

setup(name='tion',
      version='1.23',
      description='Tion Magic Air API',
      url='http://github.com/airens/tion',
      author='Valeriy Chistyakov',
      author_email='airens@mail.ru',
      license='MIT',
      packages=['tion'],
      install_requires=['requests'],
      zip_safe=False,
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      long_description_content_type="text/markdown"
      )
