import sys

# setup.py
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name="Math Operations",
    version="1.2.1",
    description="Simple Math Operations using Python QT Framework",
    executables=[Executable("main.py",base=base)],
    options={
        'build_exe': {
            'include_files': ['main.py','operations.py','operations.txt'],
            'packages' : ['sys','PyQt5.QtGui','PyQt5.QtWidgets']
        }
    }
)

