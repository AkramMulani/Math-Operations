import sys

from PyQt5.QtGui import QIntValidator, QFont

from operations import Operations
from PyQt5.QtWidgets import *

def addOperation():
    label_name = QLabel('Name')
    input_name = QLineEdit()
    input_name.setFixedWidth(200)
    label_define = QLabel('Define Operation')
    input_define = QLineEdit()
    input_define.setFixedWidth(200)
    layout = QVBoxLayout()
    layout.addWidget(label_name)
    layout.addWidget(input_name)
    layout.addWidget(label_define)
    layout.addWidget(input_define)
    submit_b = QPushButton('Submit')
    cancel_b = QPushButton('Cancel')
    dialog = QDialog()
    def submit():
        name = input_name.text()
        define = input_define.text()
        if name.strip()!='' and define.strip()!='':
            operation.addOperation(name,define)
            combo_box.addItem(name)
            dialog.accept()
        else:
            QMessageBox.warning(dialog,'Warning','Please enter valid information')

    def cancel():
        dialog.reject()

    submit_b.clicked.connect(submit)
    cancel_b.clicked.connect(cancel)
    layout.addWidget(submit_b)
    layout.addWidget(cancel_b)
    dialog.setLayout(layout)
    dialog.exec_()

def start():
    app = QApplication(sys.argv)

    global frame
    frame = QWidget()
    frame.setWindowTitle('Math Operations')
    frame.setGeometry(100, 100, 1300, 800)

    # For adding new operations
    add_operation_label = QLabel('Add New Operation')
    add_operation_label.setFont(QFont('Arial', 12))
    add_operation_label.setFixedWidth(300)
    add_operation_button = QPushButton('+')
    add_operation_button.setFixedSize(70,50)
    add_operation_button.setFont(QFont('Arial',15))
    add_operation_button.clicked.connect(addOperation)

    # selection list
    select_label = QLabel('Select Operation')
    select_label.setFont(QFont('Arial',12))
    select_label.setFixedSize(200,50)
    global combo_box
    combo_box = QComboBox()
    available_operations = operation.getOperations()
    for name,definition in available_operations.items():
        combo_box.addItem(name)
    combo_box.setFont(QFont('Arial',12))
    combo_box.setFixedSize(250,50)

    number1_label = QLabel('Number 1 ')
    number1_label.setFont(QFont('Arial',12))
    number1_label.setFixedWidth(200)
    number1_edit = QLineEdit()
    number1_edit.setFixedSize(200,50)
    number1_edit.setValidator(QIntValidator())
    number1_edit.setFont(QFont('Arial',15))

    number2_label = QLabel('Number 2 ')
    number2_label.setFont(QFont('Arial',12))
    number2_label.setFixedWidth(200)
    number2_edit = QLineEdit()
    number2_edit.setFixedSize(200, 50)
    number2_edit.setValidator(QIntValidator())
    number2_edit.setFont(QFont('Arial', 15))

    result_label = QLabel('Result ')
    result_label.setFont(QFont('Arial',12))
    result_label.setFixedWidth(200)
    result_edit = QLineEdit()
    result_edit.setFixedSize(200,50)
    result_edit.setValidator(QIntValidator())
    result_edit.setFont(QFont('Arial',15))

    evaluate_button = QPushButton('Evaluate')
    evaluate_button.setFont(QFont('Arial',12))
    evaluate_button.setFixedWidth(200)
    def evaluate():
        num1 = number1_edit.text()
        num2 = number2_edit.text()
        if num1.strip()!='' and num2.strip()!='':
            result = operation.evaluate_expression(int(num1),int(num2),combo_box.currentText())
            if result[0]:
                result_edit.setText(result[1])
            else:
                result_edit.setText(f'Math Error:{result[1]}')
        else:
            QMessageBox.warning(frame,'Warning','Please enter operands to perform operations')

    evaluate_button.clicked.connect(evaluate)

    # Vertical layout
    vertical_layout = QVBoxLayout()

    # Horizontal layout
    # For new operations
    add_operation_layout = QHBoxLayout()
    add_operation_layout.addWidget(add_operation_label)
    add_operation_layout.addWidget(add_operation_button)
    add_operation_layout.addWidget(select_label)
    add_operation_layout.addWidget(combo_box)

    # Input Number 1
    number1_layout = QHBoxLayout()
    number1_layout.addWidget(number1_label)
    number1_layout.addWidget(number1_edit)

    # Input Number 2
    number2_layout = QHBoxLayout()
    number2_layout.addWidget(number2_label)
    number2_layout.addWidget(number2_edit)

    # Output Result
    result_layout = QHBoxLayout()
    result_layout.addWidget(result_label)
    result_layout.addWidget(result_edit)

    # evaluation part
    evaluate_layout = QHBoxLayout()
    evaluate_layout.addWidget(evaluate_button)

    vertical_layout.addLayout(add_operation_layout)
    vertical_layout.addLayout(number1_layout)
    vertical_layout.addLayout(number2_layout)
    vertical_layout.addLayout(result_layout)
    vertical_layout.addLayout(evaluate_layout)

    frame.setLayout(vertical_layout)

    frame.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    operation = Operations()
    start()
