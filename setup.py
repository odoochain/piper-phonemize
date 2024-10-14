import platform
from pathlib import Path

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

_DIR = Path(__file__).parent
_LIB_DIR = _DIR / "_install/lib"
_INCLUDE_DIR = _DIR / '_install/include'


__version__ = "1.1.0"

ext_modules = [
    Pybind11Extension(
        "piper_phonemize_cpp",
        [
            "src/python.cpp",
            "src/phonemize.cpp",
            "src/phoneme_ids.cpp",
            "src/tashkeel.cpp",
        ],
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=[str(_INCLUDE_DIR)],
        library_dirs=[str(_LIB_DIR)],
        libraries=["espeak-ng", "onnxruntime"],
    ),
]

setup(
    name="piper-phonemize",
    version=__version__,
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    url="https://github.com/rhasspy/piper-phonemize",
    description="Phonemization libary used by Piper text to speech system",
    long_description="",
    packages=["piper_phonemize"],
    package_data={
        "piper_phonemize": [
            str(p) for p in (_DIR / "piper_phonemize" / "espeak-ng-data").rglob("*")
        ]
        + [str(_DIR / "libtashkeel_model.ort")],
        '': [str(p) for p in (_DIR / "piper_phonemize").rglob("*.dll")]
        + [str(p) for p in (_DIR / "piper_phonemize").rglob("*.so*")]
    

    },
    include_package_data=True,
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
