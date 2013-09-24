from setuptools import setup

requires = open('requirements.txt').read().split('\n')

setup(
    name = 'unn',
    version = '0.0.13',
    packages = ['unn',],
    scripts = ['unn/unn'],
    license = 'MIT',
    install_requires = requires,
    description = "The most minimal blog engine you've never heard of",
    long_description = open('README.md').read(),
)
