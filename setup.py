
from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirement_file:
    requirements = requirement_file.read().splitlines()
    print(requirements)

setup(
    name='demo',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages("src"),
    install_requires=requirements,
)