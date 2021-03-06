from setuptools import setup, find_packages

setup(
    long_description=open("README.rst", "r").read(),
    name="pybt-smthnspcl",
    version="0.43",
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
