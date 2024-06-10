import overlay_lib
from overlay_lib import *
from PyQt5 import QtWidgets, QtCore

class ChildWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        
        self.setWindowTitle("GuiTest")
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.oldPos
        self.window().move(self.window().pos() + delta)
        self.oldPos = event.globalPos() 

def callback():
    return [
        FlDrawRect(Vector2D(960, 540), 200, 200, RgbaGradient(RgbaColor(255, 255, 0, 10), RgbaColor(255, 0, 255, 40)), RgbaColor(255, 255, 255, 255), 1)
    ]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    guiWindow=ChildWindow,
    refreshTimeout=1
)

overlay.spawn()