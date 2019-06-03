from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    install_requires=[],
    url='https://github.com/djankooo/cipherPackage',
    author='Jan Kamuda',
    author_email='218202@student.pwr.edu.pl'
)