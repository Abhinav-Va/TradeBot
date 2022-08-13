from setuptools import setup, find_packages

setup(
    name='tradebot',
    version='0.1.0',
    packages=find_packages(include=['tradebot', 'tradebot.*']),
    install_requires=[
        'python-decouple',
        'config',
        'decouple',
        'requests'
    ]
)