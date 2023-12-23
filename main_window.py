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