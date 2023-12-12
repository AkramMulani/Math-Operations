import sys

from PyQt5.QtWidgets import QApplication

from gui.GuiHandler import GUIHandler

from operations import Operations

app = QApplication(sys.argv)
operation = Operations()
window = GUIHandler(operation)
sys.exit(app.exec_())