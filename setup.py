import os, sys

HOME_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(HOME_DIR, 'eenum.py'))

from eenum import __version__

readme = os.path.join(HOME_DIR, 'README.rst')
long_description = open(readme).read()

install_requires = [
    'six>=1.10',
]

if sys.version_info[:2] < (3,4):
    install_requires.append('enum34>=1.0.4')


readme = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme).read()


SETUP_ARGS = dict(
    name='eenum',
    version=__version__,
    description=('Extension to the python enum and Enum3.4 libraries'),
    long_description=long_description,
    url='https://github.com/cltrudeau/eenum',
    author='Christopher Trudeau',
    author_email='ctrudeau+pypi@arsensa.com',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='tools,enum',
    test_suite='load_tests.get_suite',
    py_modules = ['waelstow',],
    install_requires=install_requires,
)

if __name__ == '__main__':
    from setuptools import setup
    setup(**SETUP_ARGS)
