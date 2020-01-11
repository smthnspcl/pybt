from setuptools import setup, find_packages
from sys import version_info
from os import system

v = '{0]{1}'.format(version_info[0], version_info[1])
system("cd /tmp/;"
       "pip3 download gattlib;"
       "tar xvzf ./gattlib-0.20150805.tar.gz;"
       "cd gattlib-0.20150805/;"
       "sed -ie 's/boost_python-py34/boost_python{0}/' setup.py;"
       "pip3 install ."
       "cd .."
       "rm -rf gattlib-0.20150805/".format(v))


setup(
    long_description_content_type="text/markdown",
    long_description=open("readme.md", "r").read(),
    name="pybt",
    version="0.42",
    description="bluetooth library",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/pybt",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="bluetooth library",
    packages=find_packages(),
)
