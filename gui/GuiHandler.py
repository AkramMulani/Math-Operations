
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout, \
    QMessageBox

from PyQt5.QtGui import QFont,QIcon,QIntValidator,QDoubleValidator

from PyQt5.QtCore import Qt

from gui.dialogs import CustomDialog
from operations import Operations


class GUIHandler(QWidget):
    def __init__(self,operation:Operations):
        super().__init__()

        self._OP_ = operation

        # application icon
        self.ICON = QIcon('./assets/icon.ico')

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
        self._SELECTED_EXPRESSION_LABEL_ = QLabel()
        self._LITERALS_LABELS_ = list()
        self._RESULT_LABEL_ = QLabel('Result')

        # buttons used in application
        self._ADD_OPERATION_BUTTON_ = QPushButton('+')
        self._DELETE_OPERATION_BUTTON_ = QPushButton('-')
        self._EVALUATE_EXPRESSION_BUTTON_ = QPushButton('Evaluate')
        self._CLEAR_INPUT_BUTTON_ = QPushButton('Clear')

        # One line text editor used in application
        self._LINE_EDITS_ = list()
        self._RESULT_LINE_EDIT_ = QLineEdit()

        # combo box for selecting operation
        self._SELECT_COMBO_BOX_ = QComboBox()

        # custom dialogs for adding operation and removing operations
        self._ADD_OPERATION_DIALOG_ = CustomDialog(self, self._OP_)
        self._DELETE_OPERATION_DIALOG_ = CustomDialog(self, self._OP_)

        # layouts
        self._FORM_LAYOUT_ = QFormLayout()
        self._BOX_LAYOUT_HORIZONTAL_ = QHBoxLayout()
        self._BOX_LAYOUT_HORIZONTAL_1_ = QHBoxLayout()
        self._BOX_LAYOUT_VERTICAL = QVBoxLayout()

        self._initGui_()

    def _initGui_(self):
        self.setWindowTitle('Math Operations')
        self.setWindowIcon(self.ICON)
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(1200, 800)
        self.setMaximumSize(1200, 800)
        self.setStyleSheet("""
                    QWidget {
                        background-color: #f0f0f0;
                    }
                    QLabel {
                        font-size: 20px;
                        color: #333;
                    }
                    QLineEdit {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                        font-size: 18px;
                    }
                """)
        self._create_literal_inputs_()
        self._add_components_()
        self._setStyles_()
        self.show()

    def _add_components_(self):
        self._BOX_LAYOUT_HORIZONTAL_.addWidget(self._ADD_OPERATION_BUTTON_)
        self._BOX_LAYOUT_HORIZONTAL_.addWidget(self._DELETE_OPERATION_BUTTON_)
        self._FORM_LAYOUT_.addRow(self._ADD_DELETE_OPERATION_LABEL_, self._BOX_LAYOUT_HORIZONTAL_)
        self._FORM_LAYOUT_.addRow(self._SELECT_OPERATION_LABEL_, self._SELECT_COMBO_BOX_)
        self._FORM_LAYOUT_.addRow(self._SELECTED_EXPRESSION_LABEL_)
        self._FORM_LAYOUT_.addRow(self._RESULT_LABEL_, self._RESULT_LINE_EDIT_)
        self._BOX_LAYOUT_HORIZONTAL_1_.addWidget(self._EVALUATE_EXPRESSION_BUTTON_)
        self._BOX_LAYOUT_HORIZONTAL_1_.addWidget(self._CLEAR_INPUT_BUTTON_)
        self._FORM_LAYOUT_.addRow(self._BOX_LAYOUT_HORIZONTAL_1_)
        self.setLayout(self._FORM_LAYOUT_)
        self._setButtons_()

    def _setButtons_(self):
        self._ADD_OPERATION_BUTTON_.setFixedWidth(100)
        self._DELETE_OPERATION_BUTTON_.setFixedWidth(100)
        self._EVALUATE_EXPRESSION_BUTTON_.setFixedWidth(230)
        self._CLEAR_INPUT_BUTTON_.setFixedWidth(250)
        self._ADD_OPERATION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._DELETE_OPERATION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._EVALUATE_EXPRESSION_BUTTON_.setCursor(self._BUTTON_CURSOR_)
        self._CLEAR_INPUT_BUTTON_.setCursor(self._BUTTON_CURSOR_)

        self._ADD_OPERATION_BUTTON_.clicked.connect(self._on_add_operation_click_)
        self._DELETE_OPERATION_BUTTON_.clicked.connect(self._on_delete_operation_click_)
        self._EVALUATE_EXPRESSION_BUTTON_.clicked.connect(self._on_evaluate_expression_click_)
        self._CLEAR_INPUT_BUTTON_.clicked.connect(self._on_clear_input_click_)

        self._ADD_OPERATION_BUTTON_.setToolTip('Add your custom operations')
        self._DELETE_OPERATION_BUTTON_.setToolTip('Delete operation from list')
        self._EVALUATE_EXPRESSION_BUTTON_.setToolTip('Evaluate Expression')
        self._CLEAR_INPUT_BUTTON_.setToolTip('Clear Input')
        self._setComboBox_()

    def _setComboBox_(self):
        self._SELECT_COMBO_BOX_.setFixedWidth(500)
        self._SELECT_COMBO_BOX_.setCursor(self._BUTTON_CURSOR_)
        self._SELECT_COMBO_BOX_.currentIndexChanged.connect(self._create_literal_inputs_)
        self._SELECT_COMBO_BOX_.setStyleSheet("""
            QComboBox {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                        selection-background-color: #f0f0f0;
                        font-size: 20px;
                    }
        """)
        for op,ex in self._OP_.getOperations().items():
            self._SELECT_COMBO_BOX_.addItem(op)
        self._set_combo_box_tooltips_()
        self._setLineEdit_()

    def _setLineEdit_(self):
        self._RESULT_LINE_EDIT_.setFixedWidth(500)

    def _create_literal_inputs_(self):
        self._RESULT_LINE_EDIT_.clear()
        selected_operation = self._SELECT_COMBO_BOX_.currentText()
        operation_dict = self._OP_.getOperations()
        row_to_insert = 3 # inserting row in form

        if selected_operation in operation_dict:
            operation_expression = operation_dict[selected_operation]
            self._SELECTED_EXPRESSION_LABEL_.setText(f'Expression: {operation_expression["define"]}, Date: {operation_expression["time"]}')
            literals = []

            # Extract literals while preserving their order
            for char in operation_expression['define']:
                if char.isalpha() and char not in literals:
                    literals.append(char)

            self._clear_literal_inputs_()  # Clear previous inputs

            for i, literal in enumerate(literals):
                label = QLabel(f'Label {literal}:')
                line_edit = QLineEdit()
                line_edit.setValidator(self._DOUBLE_VALIDATOR_)
                line_edit.setFixedWidth(500)
                label.setStyleSheet("""
                    QLabel {
                        font-size: 20px;
                        color: #333;
                    }
                """)
                line_edit.setStyleSheet("""
                    QLineEdit {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                        font-size: 18px;
                    }
                """)
                self._LITERALS_LABELS_.append(label)
                self._LINE_EDITS_.append(line_edit)
                self._FORM_LAYOUT_.insertRow(row_to_insert, label, line_edit)
                row_to_insert+=1
        else:
            self._SELECTED_EXPRESSION_LABEL_.setText('Expression not selected')
            self._clear_literal_inputs_()

    def _clear_literal_inputs_(self):
        for label in self._LITERALS_LABELS_:
            label.setParent(None)
            label.deleteLater()
        for line_edit in self._LINE_EDITS_:
            line_edit.setParent(None)
            line_edit.deleteLater()

        self._LITERALS_LABELS_.clear()
        self._LINE_EDITS_.clear()

    def _setStyles_(self):
        # Set styles for buttons
        self._ADD_OPERATION_BUTTON_.setStyleSheet("""
            QPushButton {
                background-color: rgb(61, 207, 112);
                color: white; 
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 20px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(34, 158, 77);
            }
        """)
        self._DELETE_OPERATION_BUTTON_.setStyleSheet("""
            QPushButton {
                background-color: rgb(212, 43, 43);
                color: white; 
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 20px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(180, 21, 21);
            }
        """)
        self._EVALUATE_EXPRESSION_BUTTON_.setStyleSheet("""
            QPushButton {
                background-color: rgb(72, 145, 209);
                color: white; 
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 20px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(25, 135, 150);
            }
        """)
        self._CLEAR_INPUT_BUTTON_.setStyleSheet("""
            QPushButton {
                background-color: rgb(89, 94, 95);
                color: white; 
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 20px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: rgb(65, 68, 68);
            }
        """)

    def _update_combo_box_(self):
        # clear combo box
        self._SELECT_COMBO_BOX_.clear()
        # adding dictionary to box:
        for name,exp in self._OP_.getOperations().items():
            self._SELECT_COMBO_BOX_.addItem(name)
        self._set_combo_box_tooltips_()

    def _set_combo_box_tooltips_(self):
        operation_dict = self._OP_.getOperations()

        for i in range(self._SELECT_COMBO_BOX_.count()):
            combo_box_item_text = self._SELECT_COMBO_BOX_.itemText(i)
            if combo_box_item_text in operation_dict.keys():
                expression = operation_dict[combo_box_item_text]
                tooltip_text = f"Expression: {expression['define']}, Date: {expression['time']}"
                self._SELECT_COMBO_BOX_.setItemData(i, tooltip_text, Qt.ToolTipRole)

    def _on_add_operation_click_(self):
        self._ADD_OPERATION_DIALOG_.set_add_frame()
        self._ADD_OPERATION_DIALOG_.__add_operation__()
        self._ADD_OPERATION_DIALOG_.exec_()
        self._update_combo_box_()

    def _on_delete_operation_click_(self):
        if self._OP_.getOperations():
            self._DELETE_OPERATION_DIALOG_.set_delete_frame()
            self._DELETE_OPERATION_DIALOG_.__delete_operation__()
            self._DELETE_OPERATION_DIALOG_.exec_()
            self._update_combo_box_()
        else:
            QMessageBox.warning(self,'Warning','Operation dictionary is empty!')

    def _on_evaluate_expression_click_(self):
        selected_operation = self._SELECT_COMBO_BOX_.currentText()
        operation_dict = self._OP_.getOperations()

        if selected_operation in operation_dict:
            expression = operation_dict[selected_operation]['define']
            literals_in_expression = []

            # Extract literals
            for char in expression:
                if char.isalpha() and char not in literals_in_expression:
                    literals_in_expression.append(char)
            # print(literals_in_expression)

            literal_values = [line_text.text() for line_text in self._LINE_EDITS_]
            # print(literal_values)

            for val in literal_values:
                if val.strip()=='':
                    QMessageBox.warning(self,'Warning','Please fill the all literal values!')
                    return

            kwargs = {literal: val for literal, val in zip(literals_in_expression, literal_values)}

            result = self._OP_.evaluate_expression(selected_operation, **kwargs)

            if result[0] == 1:
                # Handle successful result
                self._RESULT_LINE_EDIT_.setText(result[1])
                # print(f"Result: {result[1]}")
            else:
                # Handle error
                self._RESULT_LINE_EDIT_.setText(f'Error:{result[1]}')
                # print(f"Error: {result[1]}")

    def _on_clear_input_click_(self):
        self._clear_literal_inputs_()
        self._create_literal_inputs_()
        self._RESULT_LINE_EDIT_.clear()