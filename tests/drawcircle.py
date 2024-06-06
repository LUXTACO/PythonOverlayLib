import overlay_lib
from overlay_lib import Vector2D, RgbaTuple, DrawCircle

def callback():
    return [DrawCircle(Vector2D(960, 540), 10, RgbaTuple(255, 255, 255, 255), 1)]

overlay = overlay_lib.Overlay(
    drawlistCallback=callback,
    refreshTimeout=1
)

overlay.spawn()