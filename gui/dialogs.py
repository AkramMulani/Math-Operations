
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QHBoxLayout, \
    QListWidget, QMessageBox

from operations import Operations

class CustomDialog(QDialog):
    def __init__(self,frame:QWidget,option:int,operation:Operations):
        super().__init__(frame)
        self._OP_ = operation
        self._function_call = None
        if option == 1:
            self.setGeometry(900,200,300,150)
            self.__function_call__ = self._add_operation_
        elif option == 2:
            self.setGeometry(900, 200, 300, 250)
            self.__function_call__ = self._delete_operation_
        self.setStyleSheet("""
                    QDialog {
                        background-color: #f0f0f0;
                        border: 1px solid #aaa;
                        border-radius: 5px;
                    }
                    QLabel {
                        font-size: 14px;
                        color: #333;
                    }
                    QLineEdit, QListWidget {
                        padding: 8px;
                        border-radius: 5px;
                        border: 1px solid #ccc;
                        background-color: #fff;
                    }
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        padding: 8px 16px;
                        font-size: 14px;
                        margin-top: 8px;
                        margin-right: 8px;
                        cursor: pointer;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                """)

    def _add_operation_(self):
        name = QLabel('Name:')
        name_text = QLineEdit()
        define = QLabel('Define:')
        define_text = QLineEdit()

        def submit():
            if name_text.text().strip()!='' and define_text.text().strip()!='':
                self._OP_.addOperation(name_text.text().strip(),define_text.text().strip())
                self.accept()
            else:
                QMessageBox.warning(self,'Warning','Please enter valid inputs!')

        def cancel():
            self.reject()

        frame_layout = QFormLayout()
        frame_layout.addRow(name,name_text)
        frame_layout.addRow(define,define_text)

        submit_btn = QPushButton('Submit')
        cancel_btn = QPushButton('Cancel')
        submit_btn.clicked.connect(submit)
        cancel_btn.clicked.connect(cancel)

        box_layout_h = QHBoxLayout()
        box_layout_h.addWidget(submit_btn)
        box_layout_h.addWidget(cancel_btn)

        box_layout = QVBoxLayout()
        box_layout.addLayout(frame_layout)
        box_layout.addLayout(box_layout_h)

        self.setLayout(box_layout)

    def _delete_operation_(self):
        label = QLabel('Select Operation to delete')
        o_list = QListWidget()
        for op in self._OP_.getOperations().keys():
            o_list.addItem(op)
        def submit():
            index = o_list.row(o_list.currentItem())
            i = self._OP_.removeOperation(index)
            if not i:
                QMessageBox.warning(self,'Warning','Something went wrong!')
            else:
                o_list.takeItem(index)
                self.accept()

        def cancel():
            self.reject()

        submit_btn = QPushButton('Submit')
        cancel_btn = QPushButton('Cancel')

        submit_btn.clicked.connect(submit)
        cancel_btn.clicked.connect(cancel)

        h_layout = QHBoxLayout()
        h_layout.addWidget(submit_btn)
        h_layout.addWidget(cancel_btn)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(o_list)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)