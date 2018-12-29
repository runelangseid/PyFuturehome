# @todo Change strings
from setuptools import setup

setup(name='pyfuturehome',
      version='0.1',
      description='Interacts with the Futurehome API',
      url='http://github.com/runelangseid/pyfuturehome',
      author='Rune Langseid',
      author_email='runelangseid@gmail.com',
      license='MIT',
      packages=['pyfuturehome'],
      install_requires=[
          'requests',
      ],      zip_safe=False)
