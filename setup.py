from distutils.core import setup

requires = open('requirements.txt').read().split('\n')

setup(
    name = 'unn',
    version = '0.0.6',
    packages = ['unn',],
    scripts = ['unn/unn'],
    license = 'MIT',
    requires = requires,
    long_description = open('README.md').read(),
)
