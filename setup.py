from setuptools import setup

requires = open('requirements.txt').read().split('\n')
requires = [' (=='.join(x.split('==')) + ')' for x in requires if x]

setup(
    name = 'unn',
    version = '0.0.7',
    packages = ['unn',],
    scripts = ['unn/unn'],
    license = 'MIT',
    install_requires = requires,
    long_description = open('README.md').read(),
)
