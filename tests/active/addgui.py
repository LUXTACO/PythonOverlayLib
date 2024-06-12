import sys
import overlay_lib
from overlay_lib import *
from PyQt5 import QtWidgets, QtCore

class ChildWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        
        self.isShowing = True
        
        self.setWindowTitle("GuiTest")
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        
        self.header = QtWidgets.QFrame(self)
        self.header.setGeometry(0, 0, 1000, 50)
        self.header.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        
        self.title = QtWidgets.QLabel(self.header)
        self.title.setGeometry(0, 0, 1000, 50)
        self.title.setText("GuiTest")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet("color: white; font-size: 20px;")
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Insert and self.isShowing:
            self.setWindowOpacity(0)
        elif event.key() == QtCore.Qt.Key_Insert and not self.isShowing:
            self.setWindowOpacity(1)
            
        self.isShowing = not self.isShowing
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.oldPos
        self.window().move(self.window().pos() + delta)
        self.oldPos = event.globalPos() 

def callback():
    return [
        FlDrawRect(Vector2D(960, 540), 200, 200, RgbaGradient(RgbaColor(255, 255, 0, 10), RgbaColor(255, 0, 255, 40)), RgbaColor(255, 0, 255, 255), 1)
    ]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    guiWindow=ChildWindow,
    refreshTimeout=1
)

overlay.spawn()