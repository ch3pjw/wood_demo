from setuptools import setup, find_packages

setup(
    name='wood_demo',
    description='Example pipe flow calculation package',
    keywords=['pipe', 'fluid', 'flow'],
    url='',
    author='Paul Weaver',
    author_email='paul@concertdaw.co.uk',
    version='0.0.0',
    license='',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'test': ['flake8']
    },
    entry_points={
        'console_scripts': [
        ]
    }
)
