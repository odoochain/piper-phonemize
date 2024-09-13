# Building

```console
python -m venv venv
source venv/bin/activate
pip install setuptools pybind11 build

cmake -B build -DCMAKE_INSTALL_PREFIX=_install
cmake --build build --config Release
cmake --install build
```

_On macOS and Linux_

```console
export CPPFLAGS="-I${PWD}/_install/include/piper-phonemize -I${PWD}/_install/include -L${PWD}/_install/lib"
cp -rf ./_install/share/espeak-ng-data ./piper_phonemize/
python setup.py clean --all
python -m build -w
```

_On macOS__

```console
pip install delocate
export DYLD_LIBRARY_PATH=$(pwd)/_install/lib
delocate-wheel -w fixed_wheels -v ./dist/piper_phonemize*.whl
```

_On Windows_

```console
Copy-Item -Recurse ./_install/share/espeak-ng-data ./piper_phonemize/
$env:INCLUDE += ";$pwd/_install/include"
$env:LIB += ";$pwd/_install/lib"
Copy-Item _install\bin\espeak-ng.dll piper_phonemize\
Copy-Item _install\lib\onnxruntime.dll piper_phonemize\
python -m build -w
```

_On Linux WIP_

```console
cp -rf _install/lib/*.so* piper_phonemize/
python -m build -w
```

__Debug pyd dependencies with___

https://github.com/lucasg/Dependencies/releases/tag/v1.11.1

## Publish

Prepare token from https://pypi.org/manage/account/

```console
pip install setuptools wheel twine
export TWINE_PASSWORD="token"
twine upload dist/*
```
