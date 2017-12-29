from setuptools import setup

setup(name='UDON_scripts',
      version='0.1',
      description='Download songs and process them',
      url='https://www.github.com/UDONRadio/UDON_scripts',
      author='Matthew Deville',
      author_email='kemiimek@live.fr',
      license='MIT',
      packages=['UDON_scripts'],
      install_requires=['youtube_dl', 'eyed3'],
      zip_safe=False)
