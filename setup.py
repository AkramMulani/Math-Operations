import sys

# setup.py
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name="Math Operations",
    version="1.2.4",
    description="Simple Math Operations using Python QT Framework",
    executables=[Executable("main.py",base=base,shortcutName='Math Operations',icon='assets/icon.png')],
    options={
        'build_exe': {
            'include_files': ['main.py','operations.py','operations.txt','gui/dialogs.py','gui/GuiHandler.py','assets/icon.png'],
            'packages' : ['sys','PyQt5.QtGui','PyQt5.QtWidgets','PyQt5.QtCore','datetime']
        }
    }
)

