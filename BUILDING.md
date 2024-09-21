# Building

```console
python -m venv venv
source venv/bin/activate
pip install setuptools pybind11 build

cmake -B build -DCMAKE_INSTALL_PREFIX=_install
cmake --build build --config Release
cmake --install build
export CPPFLAGS="-I${PWD}/_install/include/piper-phonemize -I${PWD}/_install/include -L${PWD}/_install/lib"
cp -rf ./_install/share/espeak-ng-data ./piper_phonemize/
python -m build -w
```

_On macOS__

```console
pip install delocate
export DYLD_LIBRARY_PATH=$(pwd)/_install/lib
delocate-wheel -w fixed_wheels -v ./dist/piper_phonemize*.whl
```