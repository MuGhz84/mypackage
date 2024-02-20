from setuptools import setup, find_packages

setup(
   name='mypackage',
   version='0.1',
   #packages=['foo'],  #same as name
   packages=find_packages(exclude='tests*'),
   license='MIT',
   description='EDSA example python package',
   long_description=open('README.md').read(),
   install_requires=['numpy'], #external packages as dependencies
   url='https://github.com/MuGhz84',
   author='M. GHz',
   author_email='M.GHz@gmail.example'
)