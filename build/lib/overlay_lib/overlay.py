import ctypes
from .classes import *
from PyQt5 import QtGui
from typing import Callable, Any
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPen, QColor, QImage

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
            #? Skeleton Draws
            if isinstance(item, SkDrawRect):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawRect(item.coords.x, item.coords.y, item.width, item.height)
            elif isinstance(item, SkDrawCircle):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawEllipse(QPoint(int(item.coords.x), int(item.coords.y)), item.radius, item.radius)
            
            #? Filled Draws
            elif isinstance(item, FlDrawRect):
                if isinstance(item.fill_color, RgbaColor): #> If is Color (RgbaColor) >> Solid Color
                    painter.setBrush(QtGui.QBrush(QtGui.QColor(item.fill_color.r, item.fill_color.g, item.fill_color.b, item.fill_color.a)))
                elif isinstance(item.fill_color, RgbaGradient): #> If is Gradient (RgbaGradient) >> Linear Gradient
                    gradient = QtGui.QLinearGradient(item.coords.x, item.coords.y, item.coords.x + item.width, item.coords.y + item.height)
                    gradient.setColorAt(0, QtGui.QColor(item.fill_color.from_rgba.r, item.fill_color.from_rgba.g, item.fill_color.from_rgba.b, item.fill_color.from_rgba.a))
                    gradient.setColorAt(1, QtGui.QColor(item.fill_color.to_rgba.r, item.fill_color.to_rgba.g, item.fill_color.to_rgba.b, item.fill_color.to_rgba.a))
                    painter.setBrush(QtGui.QBrush(gradient))
                painter.setPen(QtGui.QPen(QtGui.QColor(item.outline_color.r, item.outline_color.g, item.outline_color.b, item.outline_color.a), item.thickness))
                painter.drawRect(item.coords.x, item.coords.y, item.width, item.height)
            elif isinstance(item, FlDrawCircle):
                if isinstance(item.fill_color, RgbaColor):
                    painter.setBrush(QtGui.QBrush(QtGui.QColor(item.fill_color.r, item.fill_color.g, item.fill_color.b, item.fill_color.a)))
                elif isinstance(item.fill_color, RgbaGradient):
                    gradient = QtGui.QRadialGradient(item.coords.x, item.coords.y, item.radius)
                    gradient.setColorAt(0, QtGui.QColor(item.fill_color.from_rgba.r, item.fill_color.from_rgba.g, item.fill_color.from_rgba.b, item.fill_color.from_rgba.a))
                    gradient.setColorAt(1, QtGui.QColor(item.fill_color.to_rgba.r, item.fill_color.to_rgba.g, item.fill_color.to_rgba.b, item.fill_color.to_rgba.a))
                    painter.setBrush(QtGui.QBrush(gradient))
                painter.setPen(QtGui.QPen(QtGui.QColor(item.outline_color.r, item.outline_color.g, item.outline_color.b, item.outline_color.a), item.thickness))
                painter.drawEllipse(QPoint(int(item.coords.x), int(item.coords.y)), item.radius, item.radius)
            
            #? Normal Draws
            elif isinstance(item, DrawLine):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.drawLine(item.start_coord.x, item.start_coord.y, item.end_coord.x, item.end_coord.y)
            elif isinstance(item, DrawText):
                painter.setPen(QtGui.QPen(QtGui.QColor(item.color.r, item.color.g, item.color.b, item.color.a), item.thickness))
                painter.setFont(QtGui.QFont(item.font, item.size))
                painter.drawText(item.coords.x, item.coords.y, item.text)
            elif isinstance(item, DrawImage):
                image = QImage(item.image_path)
                painter.drawImage(item.coords.x, item.coords.y, image, item.image_position.x, item.image_position.y, item.image_size.w, item.image_size.h)
        painter.end()
 
class Overlay:
    
    def __init__(self, customSystemMetrics=None, drawlistCallback:Callable=None, guiWindow:Callable=None, refreshTimeout:int=1): 
        self.app = QtWidgets.QApplication([])
        self.overlay = MainWindow(customSystemMetrics=customSystemMetrics, drawlistCallback=drawlistCallback, refreshTimeout=refreshTimeout)
        if guiWindow is not None:
            self.gui = guiWindow()
        else:
            self.gui = None
        
    def spawn(self):
        self.overlay.show()
        if self.gui: self.gui.show()
        self.app.exec_()