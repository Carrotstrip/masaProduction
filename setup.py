"""masaProduction python package configuration."""

from setuptools import setup

setup(
    name='masaProduction',
    version='0.1.0',
    packages=['masaProduction'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.3',
        'arrow==0.10.0',
        'sh==1.12.14',
        'flask-bootstrap4'
    ],
)