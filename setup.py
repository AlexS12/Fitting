#!/usr/bin/env python
# coding: utf-8

# http://stackoverflow.com/a/10975371/554319
import io
from setuptools import setup, find_packages


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="Tomography",
    version="0.0.dev0",
    description="Master Thesis",
    author="Jaime Sáez",
    author_email="myemail@foo.com",
    download_url="https://github.com/jsaez8/Fitting/",
    license="MIT",
    keywords=[
      "Tomography",
    ],
    python_requires=">=3.5",
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "numba"
    ],
    tests_require=[
        "pytest"
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Science/Research",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.5",
      "Programming Language :: Python :: Implementation :: CPython",
      "Topic :: Scientific/Engineering",
      "Topic :: Scientific/Engineering :: Physics",
    ],
    long_description=io.open('README.md', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
)
