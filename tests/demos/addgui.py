import overlay_lib
from PyQt5 import QtWidgets, QtCore
from overlay_lib import Vector2D, RgbaTuple, DrawCircle

class ChildWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)

        # Set the window properties
        self.setGeometry(50, 50, 200, 200)

        # Create a button in the child window
        self.button = QtWidgets.QPushButton('Click me', self)
        self.button.move(50, 50)

        # Create a label in the child window
        self.label = QtWidgets.QLabel('Hello, world!', self)
        self.label.move(100, 100)

def callback():
    return [DrawCircle(Vector2D(960, 540), 10, RgbaTuple(255, 255, 255, 255), 1)]

def callback2():
    childWindow = ChildWindow(self)
    childWindow.show()
    
    return childWindow

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    guiCallback=callback2,
    refreshTimeout=1
)

overlay.spawn()