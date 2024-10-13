powershell

## piper-phonemize

下载源码并进入目录

$env:INCLUDE += ";D:\tools\piper-phonemize\include"
$env:LIB += ";D:\tools\piper-phonemize\lib"

# 安装依赖
pip install numpy<2
pip install pybind11>=2.12

setup.py临时修改为1.1.0版本

pip install .

## piper_tts

cd E:\0-odoo\2-AI\piper\src\python_run

pip install .