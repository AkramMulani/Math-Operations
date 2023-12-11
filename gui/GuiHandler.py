import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout

from PyQt5.QtGui import QFont,QIcon,QIntValidator,QDoubleValidator

from PyQt5.QtCore import Qt

from gui.dialogs import CustomDialog
from operations import Operations


class GUIHandler(QWidget):
    def __init__(self,operation:Operations):
        super().__init__()

        self._OP_ = operation

        # application icon
        self.ICON = QIcon('./assets/icon.png')

        # qt validators
        self._INT_VALIDATOR_ = QIntValidator()
        self._DOUBLE_VALIDATOR_ = QDoubleValidator()

        # cursors
        self._BUTTON_CURSOR_ = Qt.PointingHandCursor

        # fonts for components
        self._ARIAL_15_FONT_ = QFont('Arial', 15)
        self._ARIAL_12_FONT_ = QFont('Arial', 12)
        self._MONOSPACE_12_FONT_ = QFont('Monospace', 12)

        # labels used in application
        self._ADD_DELETE_OPERATION_LABEL_ = QLabel('Add/Delete Operation')
        self._SELECT_OPERATION_LABEL_ = QLabel('Select Operation')
        self._FILL_OPERANDS_VALUE_LABEL_ = QLabel('Fill All Operands Value')
        self._NUMBER_1_LABEL_ = QLabel('Number 1')
        self._NUMBER_2_LABEL_ = QLabel('Number 2')
        self._RESULT_LABEL_ = QLabel('Result')

        # buttons used in application
        self._ADD_OPERATION_BUTTON_ = QPushButton('+')
        self._DELETE_OPERATION_BUTTON_ = QPushButton('-')
        self._EVALUATE_EXPRESSION_BUTTON_ = QPushButton('Evaluate')
        self._CLEAR_INPUT_BUTTON_ = QPushButton('Clear')

        # One line text editor used in application
        self._NUMBER_1_LINE_EDIT_ = QLineEdit()
        self._NUMBER_2_LINE_EDIT_ = QLineEdit()
        self._RESULT_LINE_EDIT_ = QLineEdit()

        # combo box for selecting operation
        self._SELECT_COMBO_BOX_ = QComboBox()

        # custom dialogs for adding operation and removing operations
        self._ADD_OPERATION_DIALOG_ = CustomDialog(self, 1, self._OP_)
        self._DELETE_OPERATION_DIALOG_ = CustomDialog(self, 2, self._OP_)

        # layouts
        self._FORM_LAYOUT_ = QFormLayout()
        self._BOX_LAYOUT_HORIZONTAL_ = QHBoxLayout()
        self._BOX_LAYOUT_HORIZONTAL_1_ = QHBoxLayout()
        self._BOX_LAYOUT_VERTICAL = QVBoxLayout()

        self._initGui_()

    def _initGui_(self):
        self.setWindowTitle('Math Operations')
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(1200, 800)
        self.setMaximumSize(1200, 800)
        self.setStyleSheet("""
                    QWidget {
                        background-color: #f0f0f0;
                    }
                    QPushButton {
                        background-color: #4CAF50;
                        border: none;
                        color: white;
                        padding: 10px 24px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        transition-duration: 0.4s;
                        cursor: pointer;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QLabel {
                        font-size: 16px;
                        color: #333;
                    }
                    QLineEdit {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                    }
                    QComboBox {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                        selection-background-color: #f0f0f0;
                    }
                """)
        self._setLabels_()
        self._add_components_()
        # self._setStyles_()
        self.show()

    def _add_components_(self):
        self._BOX_LAYOUT_HORIZONTAL_.addWidget(self._ADD_OPERATION_BUTTON_)
        self._BOX_LAYOUT_HORIZONTAL_.addWidget(self._DELETE_OPERATION_BUTTON_)
        self._FORM_LAYOUT_.addRow(self._ADD_DELETE_OPERATION_LABEL_, self._BOX_LAYOUT_HORIZONTAL_)
        self._FORM_LAYOUT_.addRow(self._SELECT_OPERATION_LABEL_, self._SELECT_COMBO_BOX_)
        self._FORM_LAYOUT_.addRow(self._NUMBER_1_LABEL_, self._NUMBER_1_LINE_EDIT_)
        self._FORM_LAYOUT_.addRow(self._NUMBER_2_LABEL_, self._NUMBER_2_LINE_EDIT_)
        self._FORM_LAYOUT_.addRow(self._RESULT_LABEL_, self._RESULT_LINE_EDIT_)
        self._BOX_LAYOUT_HORIZONTAL_1_.addWidget(self._EVALUATE_EXPRESSION_BUTTON_)
        self._BOX_LAYOUT_HORIZONTAL_1_.addWidget(self._CLEAR_INPUT_BUTTON_)
        self._FORM_LAYOUT_.addRow(self._BOX_LAYOUT_HORIZONTAL_1_)
        self.setLayout(self._FORM_LAYOUT_)

    def _setLabels_(self):
        self._ADD_DELETE_OPERATION_LABEL_.setFont(self._MONOSPACE_12_FONT_)
        self._SELECT_OPERATION_LABEL_.setFont(self._ARIAL_12_FONT_)
        self._NUMBER_1_LABEL_.setFont(self._ARIAL_12_FONT_)
        self._NUMBER_2_LABEL_.setFont(self._ARIAL_12_FONT_)
        self._RESULT_LABEL_.setFont(self._ARIAL_12_FONT_)
        self._setButtons_()

    def _setButtons_(self):
        self._ADD_OPERATION_BUTTON_.setFont(self._ARIAL_15_FONT_)
        self._DELETE_OPERATION_BUTTON_.setFont(self._ARIAL_15_FONT_)
        self._EVALUATE_EXPRESSION_BUTTON_.setFont(self._ARIAL_12_FONT_)
        self._CLEAR_INPUT_BUTTON_.setFont(self._ARIAL_12_FONT_)
        self._ADD_OPERATION_BUTTON_.setFixedWidth(100)
        self._DELETE_OPERATION_BUTTON_.setFixedWidth(100)
        self._EVALUATE_EXPRESSION_BUTTON_.setFixedWidth(230)
        self._CLEAR_INPUT_BUTTON_.setFixedWidth(250)

        self._ADD_OPERATION_BUTTON_.clicked.connect(self._on_add_operation_click_)
        self._DELETE_OPERATION_BUTTON_.clicked.connect(self._on_delete_operation_click_)
        self._EVALUATE_EXPRESSION_BUTTON_.clicked.connect(self._on_evaluate_expression_click_)
        self._CLEAR_INPUT_BUTTON_.clicked.connect(self._on_clear_input_click_)

        self._ADD_OPERATION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._DELETE_OPERATION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._EVALUATE_EXPRESSION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._CLEAR_INPUT_BUTTON_.setCursor(self._BUTTON_CURSOR_)

        self._ADD_OPERATION_BUTTON_.setToolTip('Add your custom operations')
        self._DELETE_OPERATION_BUTTON_.setToolTip('Delete operation from list')
        self._EVALUATE_EXPRESSION_BUTTON_.setToolTip('Evaluate Expression')
        self._CLEAR_INPUT_BUTTON_.setToolTip('Clear Input')
        self._setComboBox_()

    def _setComboBox_(self):
        self._SELECT_COMBO_BOX_.setFont(self._ARIAL_12_FONT_)
        self._SELECT_COMBO_BOX_.setFixedWidth(500)
        self._SELECT_COMBO_BOX_.setCursor(self._BUTTON_CURSOR_)
        for op in self._OP_.getOperations().keys():
            self._SELECT_COMBO_BOX_.addItem(op)
        self._setLineEdit_()

    def _setLineEdit_(self):
        self._NUMBER_1_LINE_EDIT_.setFont(self._ARIAL_12_FONT_)
        self._NUMBER_2_LINE_EDIT_.setFont(self._ARIAL_12_FONT_)
        self._RESULT_LINE_EDIT_.setFont(self._ARIAL_12_FONT_)
        self._NUMBER_1_LINE_EDIT_.setFixedWidth(500)
        self._NUMBER_2_LINE_EDIT_.setFixedWidth(500)
        self._RESULT_LINE_EDIT_.setFixedWidth(500)
        self._NUMBER_1_LINE_EDIT_.setValidator(self._INT_VALIDATOR_)
        self._NUMBER_2_LINE_EDIT_.setValidator(self._INT_VALIDATOR_)

    def _setStyles_(self):
        # Set styles for buttons
        self._ADD_OPERATION_BUTTON_.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 8px; padding: 10px 24px; font-size: 20px;QPushButton:hover {background-color:#01FA01;}"
        )
        self._DELETE_OPERATION_BUTTON_.setStyleSheet(
            "background-color: #f44336; color: white; border-radius: 8px; padding: 10px 24px; font-size: 20px;QPushButton:hover {background-color:#ff0101;"
        )
        self._EVALUATE_EXPRESSION_BUTTON_.setStyleSheet(
            "background-color: #008CBA; color: white; border-radius: 8px; padding: 8px 16px; font-size: 16px;QPushButton:hover {background-color:#0101F0;"
        )
        self._CLEAR_INPUT_BUTTON_.setStyleSheet(
            "background-color: #555555; color: white; border-radius: 8px; padding: 8px 16px; font-size: 16px;QPushButton:hover {background-color:#100110;"
        )

        # Set styles for labels
        self._ADD_DELETE_OPERATION_LABEL_.setStyleSheet("font-size: 20px; color: #333;")
        self._SELECT_OPERATION_LABEL_.setStyleSheet("font-size: 16px; color: #333;")
        self._NUMBER_1_LABEL_.setStyleSheet("font-size: 16px; color: #333;")
        self._NUMBER_2_LABEL_.setStyleSheet("font-size: 16px; color: #333;")
        self._RESULT_LABEL_.setStyleSheet("font-size: 16px; color: #333;")

        # Set styles for line edits
        self._NUMBER_1_LINE_EDIT_.setStyleSheet(
            "padding: 8px; border-radius: 5px; border: 1px solid #ccc; background-color: #fff;"
        )
        self._NUMBER_2_LINE_EDIT_.setStyleSheet(
            "padding: 8px; border-radius: 5px; border: 1px solid #ccc; background-color: #fff;"
        )
        self._RESULT_LINE_EDIT_.setStyleSheet(
            "padding: 8px; border-radius: 5px; border: 1px solid #ccc; background-color: #fff;"
        )

        # Set styles for combo box
        self._SELECT_COMBO_BOX_.setStyleSheet(
            "padding: 8px; border-radius: 5px; border: 1px solid #ccc; background-color: #fff;"
        )

    def _update_combo_box_(self):
        # clear combo box
        self._SELECT_COMBO_BOX_.clear()
        # adding dictionary to box:
        for name in self._OP_.getOperations().keys():
            self._SELECT_COMBO_BOX_.addItem(name)

    def _on_add_operation_click_(self):
        self._ADD_OPERATION_DIALOG_.__function_call__()
        self._ADD_OPERATION_DIALOG_.exec_()
        self._update_combo_box_()

    def _on_delete_operation_click_(self):
        self._DELETE_OPERATION_DIALOG_.__function_call__()
        self._DELETE_OPERATION_DIALOG_.exec_()
        self._update_combo_box_()

    def _on_evaluate_expression_click_(self):
        if self._NUMBER_1_LINE_EDIT_.text().strip()!='' and self._NUMBER_2_LINE_EDIT_.text().strip()!='':
            result = self._OP_.evaluate_expression(
                int(self._NUMBER_1_LINE_EDIT_.text()),int(self._NUMBER_2_LINE_EDIT_.text()),
                self._SELECT_COMBO_BOX_.currentText()
            )
            if result[0]:
                self._RESULT_LINE_EDIT_.setText(result[1])
            else:
                self._RESULT_LINE_EDIT_.setText(f'Math Error:{result[1]}')

    def _on_clear_input_click_(self):
        self._NUMBER_1_LINE_EDIT_.clear()
        self._NUMBER_2_LINE_EDIT_.clear()
        self._RESULT_LINE_EDIT_.clear()