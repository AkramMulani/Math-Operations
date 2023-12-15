import sys

from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'


build_exe_options = {
    "packages": [
        "PyQt5.QtWidgets",
        "PyQt5.QtCore",
        "PyQt5.QtGui",
        "datetime",
        "sys"
    ],
    "include_files": [
        "gui/dialogs.py",
        "gui/GuiHandler.py",
        "operations.py",
        "operations.txt",
        "assets/icon.ico",
    ],
    "excludes": [
        # Exclude unnecessary parts of PyQt5
        "PyQt5.Qt",
        "PyQt5.Qt",
        "PyQt5.QtWebKit",
        "PyQt5.QtWebKitWidgets",
        "PyQt5.QtNetwork",
        "PyQt5.QtOpenGL",
        "PyQt5.QtSql",
        "PyQt5.QtXml",
        "PyQt5.phonon",
        "PyQt5.QtMultimedia",
        "PyQt5.QtPrintSupport",
        "PyQt5.QtScript",
        "PyQt5.QtScriptTools",
        "PyQt5.QtTest",
        "PyQt5.Qt3D",
        "PyQt5.QtWebEngine",
        "PyQt5.QtWebChannel",
        "PyQt5.QtPositioning",
        "PyQt5.Qml",
        "PyQt5.QtSensors",
        "PyQt5.QtBluetooth",
        "PyQt5.QtMacExtras",
        "PyQt5.QtWinExtras",
        "PyQt5.QtAndroidExtras",
        "PyQt5.QtV8",
        "PyQt5.QtV8Extras",
    ],
}

setup(
    name="Math Operations",
    version="1.2.4",
    description="Simple Math Operations using Python QT Framework",
    executables=[Executable("main.py", base=base, shortcutName='Math Operations', icon='assets/icon.ico')],
    options={
        'build_exe':build_exe_options
    }
)
