from distutils.core import setup

setup(
    name = 'unn',
    version = '0.0.4',
    packages = ['unn',],
    scripts = ['unn/unn'],
    license = 'MIT',
    long_description = open('README.md').read(),
)
