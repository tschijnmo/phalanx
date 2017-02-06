"""Setup script for phalanx."""

from setuptools import setup

DESCRIPTION = \
    'A simple parallel processing library based on MPI emulating Apache Spark'

with open('README.rst', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: System :: Distributed Computing'
]

REQUIREMENTS = [
    "mpi4py>=2.0.0",
]

setup(
    name='phalanx',
    version='0.1.0',
    author='Jinmo Zhao and Gustavo E Scuseria',
    author_email='tschijnmotschau@gmail.com',
    packages=['phalanx'],
    url='https://github.com/tschijnmo/phalanx',
    license='LICENSE',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
)
