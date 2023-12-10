
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QHBoxLayout, \
    QListWidget, QMessageBox

from operations import Operations

class CustomDialog(QDialog):
    def __init__(self,frame:QWidget,option:int,operation:Operations):
        super().__init__(frame)
        self._OP_ = operation
        self._function_call = None
        if option == 1:
            self.__function_call__ = self._add_operation_
        elif option == 2:
            self.__function_call__ = self._delete_operation_

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