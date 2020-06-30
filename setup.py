from setuptools import setuptools, find_packages

with  open('README.md') as fh:
    long_description = fh.read()


setuptools.setup(
    name='framework',
    packages=find_packages(include=['framework']),
    version='0.0.1',
    license='MIT',
    long_description= long_description,
    url='https://github.com/omnivector-solutions/framework-adapter',
    install_requires=[],
    python_requires='>=3.6',
)
