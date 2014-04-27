# coding: utf-8
import os
from setuptools import setup
import nytfrontpage

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
REQUIREMENTS = [
    line.strip() for line in open(os.path.join(os.path.dirname(__file__),
                                               'requirements.txt')).readlines()]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='nytfrontpage',
    version=nytfrontpage.__version__,
    packages=['nytfrontpage'],
    include_package_data=True,
    license='MIT License',
    description='An API for downloading frontpages from the New York Times.',
    long_description=README,
    url='https://github.com/peterldowns/nytfrontpage/',
    download_url='https://github.com/peterldowns/nytfrontpage/tarball/{}'.format(
      nytfrontpage.__version__),
    keywords=['newspaper', 'nyt', 'new york times'],
    install_requires=REQUIREMENTS,
    author='Peter Downs',
    author_email='peterldowns@gmail.com',
    classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
    ],
)

