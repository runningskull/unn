from setuptools import setup

requires = open('requirements.txt').read().split('\n')

setup(
    name = 'unn',
    version = '0.0.9',
    packages = ['unn',],
    scripts = ['unn/unn'],
    license = 'MIT',
    install_requires = requires,
    long_description = open('README.md').read(),
)
