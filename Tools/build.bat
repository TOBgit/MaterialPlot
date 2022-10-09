pyside2-uic ../matplot.ui -o ../View/matplot.py
rmdir /s /q dist
py -3 -m PyInstaller build.spec