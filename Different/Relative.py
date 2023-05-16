from __future__ import annotations

from mcpi_e.vec3 import Vec3
from copy import *


class Relative:
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    def __init__(self, position: Vec3, angle: float):
        self.position = position
        self.angle = angle
        if -45 < angle < 45:
            self.direction = Relative.SOUTH
        elif 45 <= angle < 135:
            self.direction = Relative.WEST
        elif 135 <= angle < -135:
            self.direction = Relative.NORTH
        elif -135 <= angle < -45:
            self.direction = Relative.EAST

    def get_current(self) -> Vec3:
        return self.position

    def left(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        match self.direction:
            case Relative.NORTH:
                new.position.x -= amount
            case Relative.SOUTH:
                new.position.x += amount
            case Relative.EAST:
                new.position.z -= amount
            case Relative.WEST:
                new.position.z += amount
        return new

    def right(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        match self.direction:
            case Relative.NORTH:
                new.position.x += amount
            case Relative.SOUTH:
                new.position.x -= amount
            case Relative.EAST:
                new.position.z += amount
            case Relative.WEST:
                new.position.z -= amount
        return new

    def forward(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        match self.direction:
            case Relative.NORTH:
                new.position.z -= amount
            case Relative.SOUTH:
                new.position.z += amount
            case Relative.EAST:
                new.position.x += amount
            case Relative.WEST:
                new.position.x -= amount
        return new

    def backward(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        match self.direction:
            case Relative.NORTH:
                new.position.z += amount
            case Relative.SOUTH:
                new.position.z -= amount
            case Relative.EAST:
                new.position.x -= amount
            case Relative.WEST:
                new.position.x += amount
        return new

    def bottom(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.y -= amount
        return new

    def top(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.y += amount
        return new

    def north(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.z -= amount
        return new

    def south(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.z += amount
        return new

    def east(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.x += amount
        return new

    def west(self, amount) -> Relative:
        new: Relative = deepcopy(self)
        new.position.x -= amount
        return new
