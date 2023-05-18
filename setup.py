import os
from distutils.core import setup

from setuptools import Extension
from Cython.Build import cythonize

compile_options = ["-Ofast", "-Wall"]

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_dirs = []
include_dirs = [dir_path + "/bwread/src", dir_path]

extensions = [
    Extension(
        "bwread.src.bwread",
        ["bwread/src/bwread.pyx"],
        include_dirs=include_dirs,
        library_dirs=lib_dirs,
        extra_compile_args=compile_options
    )
]

setup(ext_modules=cythonize(extensions))
