from setuptools import setup, find_packages
from pip._internal import main as pipmain
from requirements import req_array

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'geo-location-data',
    version = '0.0.1',
    description = 'geo-location-data',
    long_description = readme,
    author = 'Cole Maddox',
    author_email = 'colemaddox@protonmail.com',
    url = 'https://github.com/the-k0ru/geo-location-data',
    license = license,
    packages = find_packages(exclude=('tests', 'docs'))
)

# Install required packages
for i in req_array:
    pipmain(['install', i])