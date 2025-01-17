#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="astroARIADNE",
    version="0.5.0",
    author="Jose Vines",
    author_email="jose.vines@ug.uchile.cl",
    maintainer="Jose Vines",
    maintainer_email="jose.vines@ug.uchile.cl",
    description="Bayesian Model Averaging SED fitter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jvines/astroARIADNE",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    requires=["numpy", "scipy", "matplotlib", "astropy", "astroquery",
              "tqdm", "regions", "pyphot", "PyAstronomy", "termcolor"],
    package_data={'astroARIADNE': ['Datafiles']},
    include_package_data=True,
    python_requires='>=3.6',
)
