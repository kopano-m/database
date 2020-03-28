from setuptools import setup, find_packages

setup(
    name='database',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package to extract data from EDSA created database',
    long_description=open('README.md').read(),
    install_requires=['sqlalchemy','botocore'],
    url='https://github.com/kopano-m/database.git',
    author='Kopano Monyobo via EDSA',
    author_email='kopanomonyobo@gmail.com'
)
