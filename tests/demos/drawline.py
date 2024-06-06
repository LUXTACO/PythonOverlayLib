import overlay_lib
from overlay_lib import Vector2D, RgbaTuple, DrawLine

def callback():
    return [DrawLine(Vector2D(960, 540), Vector2D(1000, 540), RgbaTuple(255, 255, 255, 255), 1)]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    refreshTimeout=1
)

overlay.spawn()