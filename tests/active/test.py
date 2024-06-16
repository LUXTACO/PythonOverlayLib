import sys
import overlay_lib
from overlay_lib import *
from PyQt5 import QtWidgets, QtCore

def callback():
    return [
        DrawImage(Vector2D(0, 0), "./img.png"),
    ]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    refreshTimeout=1
)

overlay.spawn()