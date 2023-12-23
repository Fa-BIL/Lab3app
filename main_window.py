import sys
import os

from PyQt5 import QtWidgets

from goal_5 import Iterator
import goal_1
import goal_2
import goal_3

class ScrollLabel(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs) -> None:
        QtWidgets.QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QtWidgets.QWidget(self)
        self.setWidget(text)
        lay = QtWidgets.QVBoxLayout(text)
        self.label = QtWidgets.QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    def setText(self, text: str) -> None:
        self.label.setText(text)

class Window(QtWidgets.QWidget):
    def __init__(self) -> None:
        super(QtWidgets.QWidget, self).__init__()
        self.initUI()
        self.setStyleSheet(
            "background:rgb(255,239,213); color: rgb(48, 48, 48); font-weight:bold; border-radius: 5px;")
 