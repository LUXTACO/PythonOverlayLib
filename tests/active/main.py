import overlay_lib
from overlay_lib import Vector2D, RgbaTuple, DrawCircle, DrawLine, DrawRect, DrawText

import ctypes
user32 = ctypes.WinDLL('user32.dll')

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_mouse_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def callback():
    mouse_pos = get_mouse_position()
    return [
        DrawRect(Vector2D(mouse_pos[0], mouse_pos[1]), 300, 500, RgbaTuple(255, 255, 255, 255), 2),
        DrawCircle(Vector2D(mouse_pos[0], mouse_pos[1]), 200, RgbaTuple(255, 255, 255, 255), 2),
        DrawText(Vector2D(mouse_pos[0], mouse_pos[1]-10), 15, "Nigger Hook on top", "Arial", RgbaTuple(255, 255, 255, 255), 2),
        DrawLine(Vector2D(960, 540), Vector2D(mouse_pos[0]+150, mouse_pos[1]+250), RgbaTuple(255, 255, 255, 255), 2)
    ]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    refreshTimeout=1
)

overlay.spawn()