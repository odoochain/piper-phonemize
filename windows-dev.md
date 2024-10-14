powershell

## piper-phonemize

按照building.md来

下载源码并进入目录

$env:INCLUDE += ";D:\tools\piper-phonemize\include"
$env:LIB += ";D:\tools\piper-phonemize\lib"
$env:INCLUDE += ";D:\tools\piper-phonemize\include" # 解决h文件找不到的问题
# 安装依赖
pip install numpy<2
pip install pybind11>=2.12

setup.py临时修改为1.1.0版本

pip install .

## piper_tts
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\um\x64  增加espeak-ng.lib
C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\ucrt 增加 espeak-ng 文件夹和getopt.h onnxruntime_cxx_api.h


cd E:\0-odoo\2-AI\piper\src\python_run

pip install .