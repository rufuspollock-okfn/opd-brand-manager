import os
from setuptools import setup
from pip.req import parse_requirements

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Get requirements with PIP
install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='brand-manager',
    version='1.0',
    packages=['manager'],
    include_package_data=True,
    license='MIT License',
    description='Web brand manager of the Open Knowledge Foundation.',
    long_description=README,
    url='http://product.okfn.org/brand/',
    author='Philippe Plagnol',
    author_email='philippe.plagnol@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Natural Language :: English'
    ],
    install_requires=reqs
)
