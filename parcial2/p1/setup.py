from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "1a.pyx", compiler_directives={"language_level": "3"}
    )
)