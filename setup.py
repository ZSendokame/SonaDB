from setuptools import setup, find_packages

long_description = open('./README.md')

setup(
    name='kdb',
    version='1.0.0',
    url='https://github.com/ZSendokame/KDB',
    license='MIT license',
    author='ZSendokame',
    description='Key-Value database library, small and easy to use.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    packages=(find_packages(include=['kdb']))
)
