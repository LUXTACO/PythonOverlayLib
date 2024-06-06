from enum import Enum
from dataclasses import dataclass
from typing import Literal, NamedTuple

@dataclass
class RgbaTuple:
    r: int
    g: int
    b: int
    a: int

@dataclass
class Vector2D:
    x: int
    y: int

@dataclass   
class DrawRect:
    coords: Vector2D
    width: int
    height: int
    color: RgbaTuple
    thickness: int
    
@dataclass   
class DrawLine:
    start_coord: Vector2D
    end_coord: Vector2D
    color: RgbaTuple
    thickness: int

@dataclass 
class DrawCircle:
    coords: Vector2D
    radius: int
    color: RgbaTuple
    thickness: int

@dataclass   
class DrawText: 
    coords: Vector2D
    size: int
    text: str
    font: str
    color: RgbaTuple
    thickness: int