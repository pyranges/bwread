import os
import sys

from distutils.core import setup

from setuptools import find_packages, Extension, Command
from Cython.Build import cythonize

__version__ = open("bwread/version.py").readline().split(" = ")[1].replace(
    '"', '').strip()
macros = []

install_requires = ["numpy", "natsort", "cython", "pandas", "pyBigWig"]

compile_options = [
    "-Ofast", "-Wall"]

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_dirs = []
include_dirs = [dir_path + "/bwread/src", dir_path]

extensions = [
    Extension(
        "bwread.src.bwread",
        ["bwread/src/bwread.pyx"],
        include_dirs=include_dirs,
        library_dirs=lib_dirs,
        # language="c++",
        extra_compile_args=compile_options)
]
# libraries=["z"])]

setup(
    name="bwread",
    packages=find_packages(),
    ext_modules=cythonize(extensions, annotate=True, language_level='3'),
    package_data={'': ['*.pyx', '*.pxd', '*.h', '*.c']},
    version=__version__,
    description="Read bigwig files quickly into PyRanges",
    author="Endre Bakken Stovner",
    author_email="endrebak85@gmail.com",
    url="http://github.com/endrebak/bwread",
    license="MIT",
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta", "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Scientific/Engineering"
    ],
    include_dirs=["."],
    long_description=open("README.md").read())
