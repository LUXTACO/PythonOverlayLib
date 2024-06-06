import ctypes
from .classes import *
from PyQt5 import QtGui
from typing import Callable, Any
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPen, QColor

user32 = ctypes.WinDLL('user32.dll')

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None, customSystemMetrics:list=None, drawlistCallback:Callable=None, refreshTimeout:int=1):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Overlay")
        self.setGeometry(0, 0, (user32.GetSystemMetrics(0) if not customSystemMetrics else customSystemMetrics[0]), (user32.GetSystemMetrics(1) if not customSystemMetrics else customSystemMetrics[1]))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTransparentForInput | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.drawlist = []
        self.drawlistCallback = drawlistCallback
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_drawlist)
        self.timer.start(refreshTimeout)

    def update_drawlist(self):
        self.drawlist = self.drawlistCallback()
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for item in self.drawlist:
            if isinstance(item, DrawRect):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawRect(item.coords.x, item.coords.y, item.width, item.height)
            elif isinstance(item, DrawLine):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawLine(item.start_coord.x, item.start_coord.y, item.end_coord.x, item.end_coord.y)
            elif isinstance(item, DrawCircle):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawEllipse(QPoint(item.coords.x, item.coords.y), item.radius, item.radius)
            elif isinstance(item, DrawText):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.setFont(QtGui.QFont(item.font, item.size))
                painter.drawText(item.coords.x, item.coords.y, item.text)
        painter.end()
        
class Overlay:
    
    def __init__(self, customSystemMetrics=None, drawlistCallback:Callable=None, refreshTimeout:int=1): 
        self.app = QtWidgets.QApplication([])
        self.window = MainWindow(customSystemMetrics=customSystemMetrics, drawlistCallback=drawlistCallback, refreshTimeout=refreshTimeout)
    
    def spawn(self):
        self.window.show()
        self.app.exec_()