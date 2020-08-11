
from operator import attrgetter
from os import path
from setuptools import setup

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="win10toast",
    version="0.9",
    install_requires=install_requires,
    packages=["win10toast"],
    license="BSD",
    url="https://github.com/jithurjacob/Windows-10-Toast-Notifications",
    download_url = 'https://github.com/jithurjacob/Windows-10-Toast-Notifications/tarball/0.9',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=read('README.md'),
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
)
