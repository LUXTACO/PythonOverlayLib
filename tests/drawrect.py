import overlay_lib
from overlay_lib import Vector2D, RgbaTuple, DrawRect

def callback():
    return [DrawRect(Vector2D(960, 540), 100, 200, RgbaTuple(255, 255, 255, 255), 1)]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    refreshTimeout=1
)

overlay.spawn()