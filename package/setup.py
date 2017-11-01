from setuptools import setup

setup(name='songmanager',
      version='0.1',
      description='Download songs and process them',
      url='http://github.com/tarlyfm/UDONscripts',
      author='Matthew Deville',
      author_email='kemiimek@live.fr',
      license='MIT',
      packages=['songmanager'],
      install_requires=['youtube_dl'],
      zip_safe=False)
