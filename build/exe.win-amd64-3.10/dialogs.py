
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QHBoxLayout, \
    QListWidget, QMessageBox, QListWidgetItem

from operations import Operations

class CustomDialog(QDialog):
    def __init__(self,frame:QWidget,operation:Operations,):
        super().__init__(frame)
        self.frame = frame
        self._OP_ = operation
        self.o_list = QListWidget()
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
                """)

    def set_add_frame(self):
        self.setGeometry(800,500,300,200)

    def set_delete_frame(self):
        self.setGeometry(800,500,600,400)

    def __add_operation__(self):
        self.setWindowTitle('Add Operation')
        name = QLabel('Name:')
        name_text = QLineEdit()
        define = QLabel('Define:')
        define_text = QLineEdit()

        def submit():
            if name_text.text().strip()!='' and define_text.text().strip()!='':
                self._OP_.addOperation(name_text.text().strip(),define_text.text().strip())
                operations = list(self._OP_.getOperations().keys())
                time = f'{name_text.text().strip()} ({self._OP_.getOperations()[operations[-1]]["time"]})'
                # print(time)
                self.o_list.addItem(time)
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
        submit_btn.setStyleSheet("""
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
                        background-color: rgb(88, 145, 73);
                    }
        """)
        cancel_btn.setStyleSheet("""
                    QPushButton {
                                background-color: rgb(77, 126, 126);
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
                                background-color: rgb(87, 174, 174);
                            }
                """)

        box_layout_h = QHBoxLayout()
        box_layout_h.addWidget(submit_btn)
        box_layout_h.addWidget(cancel_btn)

        box_layout = QVBoxLayout()
        box_layout.addLayout(frame_layout)
        box_layout.addLayout(box_layout_h)

        self.setLayout(box_layout)

    def __delete_operation__(self):
        self.setWindowTitle('Delete Operation')
        label = QLabel('Select Operation to delete')
        label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                font-family: Times New Roman;
            }
        """)
        # self.o_list = QListWidget()
        self.o_list.clear()
        for op,d in self._OP_.getOperations().items():
            item = QListWidgetItem(f'{op} ({d["time"]})')
            item.setToolTip(f'Expression: {d["define"]}')
            self.o_list.addItem(item)

        def submit():
            index = self.o_list.row(self.o_list.currentItem())
            i = self._OP_.removeOperation(index)
            if not i:
                QMessageBox.warning(self,'Warning','Something went wrong!')
            else:
                self.o_list.takeItem(index)
                self.accept()

        def cancel():
            self.reject()

        submit_btn = QPushButton('Submit')
        cancel_btn = QPushButton('Cancel')
        submit_btn.clicked.connect(submit)
        cancel_btn.clicked.connect(cancel)
        submit_btn.setStyleSheet("""
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
                                background-color: rgb(88, 145, 73);
                            }
                """)
        cancel_btn.setStyleSheet("""
                            QPushButton {
                                        background-color: rgb(77, 126, 126);
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
                                        background-color: rgb(87, 174, 174);
                                    }
                        """)

        h_layout = QHBoxLayout()
        h_layout.addWidget(submit_btn)
        h_layout.addWidget(cancel_btn)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(self.o_list)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)