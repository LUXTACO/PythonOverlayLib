from enum import Enum
from dataclasses import dataclass
from typing import Literal, NamedTuple, Union

@dataclass
class RgbaColor:
    r: int
    g: int
    b: int
    a: int

@dataclass
class RgbaGradient:
    from_rgba: RgbaColor
    to_rgba: RgbaColor

@dataclass
class Vector2D:
    x: int
    y: int

#? FlDraw Dataclasses

@dataclass
class FlDrawRect:
    coords: Vector2D
    width: int
    height: int
    fill_color: Union[RgbaColor, RgbaGradient]
    outline_color: RgbaColor
    thickness: int

@dataclass 
class FlDrawCircle:
    coords: Vector2D
    radius: int
    fill_color: Union[RgbaColor, RgbaGradient]
    outline_color: RgbaColor
    thickness: int

#? SkDraw Dataclasses

@dataclass   
class SkDrawRect:
    coords: Vector2D
    width: int
    height: int
    color: RgbaColor
    thickness: int

@dataclass 
class SkDrawCircle:
    coords: Vector2D
    radius: int
    color: RgbaColor
    thickness: int

#? Draw Dataclasses
    
@dataclass   
class DrawLine:
    start_coord: Vector2D
    end_coord: Vector2D
    color: RgbaColor
    thickness: int

@dataclass   
class DrawText: 
    coords: Vector2D
    size: int
    text: str
    font: str
    color: RgbaColor
    thickness: int