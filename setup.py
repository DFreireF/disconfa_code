from setuptools import setup, find_packages
from .version import __version__

long_description = ''

try:
    from pypandoc import convert_file
    read_md = lambda f: convert_file(f, 'rst', 'md')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

classifiers = [
    'Environment :: Console',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Office/Business'
]

setup(
    name='Disconfa1988',
    packages=find_packages(),
    version=__version__,
    description='Codes used in Disconfa.',
    long_description=read_md('README.md'),
    author='DFreireF',
    url='https://github.com/DFreireF/disconfa_code',
    download_url=f'https://github.com/DFreireF/disconfa_code/tarball/{__version__}',
    entry_points={
        'console_scripts': [
            'disconfa_code = disconfa_code.__main__:main'
        ]
    },
    license='GPLv3',
    keywords=['business', 'office', 'searching', ],
    classifiers=classifiers
)