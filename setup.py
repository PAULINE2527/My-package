from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<PAULINE2527>/<My package>',
    author='<Pauline Kolobe>',
    author_email='<kolobepauline@gmail.com>'
)
