from __future__ import annotations

from mcpi_e.vec3 import Vec3
from copy import *
import Different.Direction as drctn

class Relative:
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    UP_RIGHT = 0
    UP_LEFT = 1
    DOWN_RIGHT = 2
    DOWN_LEFT = 3

    RIGHT = 0
    LEFT = 1
    FORWARD = 2
    BACKWARD = 3

    mapping_stair = {
        NORTH: {
            UP_RIGHT: drctn.UP_EAST,
            UP_LEFT: drctn.UP_WEST,
            DOWN_RIGHT: drctn.DOWN_EAST,
            DOWN_LEFT: drctn.DOWN_WEST,
        },
        SOUTH: {
            UP_RIGHT: drctn.UP_WEST,
            UP_LEFT: drctn.UP_EAST,
            DOWN_RIGHT: drctn.DOWN_WEST,
            DOWN_LEFT: drctn.DOWN_EAST,
        },
        EAST: {
            UP_RIGHT: drctn.UP_SOUTH,
            UP_LEFT: drctn.UP_NORTH,
            DOWN_RIGHT: drctn.DOWN_SOUTH,
            DOWN_LEFT: drctn.DOWN_NORTH,
        },
        WEST: {
            UP_RIGHT: drctn.UP_NORTH,
            UP_LEFT: drctn.UP_SOUTH,
            DOWN_RIGHT: drctn.DOWN_NORTH,
            DOWN_LEFT: drctn.DOWN_SOUTH,
        },
    }
    mapping_torch = {
        NORTH: {
            RIGHT: drctn.EAST,
            LEFT: drctn.WEST,
            FORWARD: drctn.NORTH,
            BACKWARD: drctn.SOUTH,
        },
        SOUTH: {
            RIGHT: drctn.WEST,
            LEFT: drctn.EAST,
            FORWARD: drctn.SOUTH,
            BACKWARD: drctn.NORTH,
        },
        EAST: {
            RIGHT: drctn.SOUTH,
            LEFT: drctn.NORTH,
            FORWARD: drctn.EAST,
            BACKWARD: drctn.WEST,
        },
        WEST: {
            RIGHT: drctn.NORTH,
            LEFT: drctn.SOUTH,
            FORWARD: drctn.WEST,
            BACKWARD: drctn.EAST,
        },
    }


    def __init__(self, position: Vec3, angle: float):
        self.position = position
        self.angle = angle
        if -45 < angle < 45:
            self.direction = Relative.SOUTH
        elif 45 <= angle < 135:
            self.direction = Relative.WEST
        elif 135 <= angle < 180 or -180 < angle < -135:
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

    def towards(self, point: Relative) -> int:
        """
        Calculates 1 dimensioned distance between current Relative and given
        :param point:
        :return:
        """
        match self.direction:
            case Relative.NORTH:
                return self.position.z - point.position.z
            case Relative.SOUTH:
                return point.position.z - self.position.z
            case Relative.EAST:
                return point.position.x - self.position.x
            case Relative.WEST:
                return self.position.x - point.position.x

    def get_stairs_abs_direction(self, direction: int) -> int:
        """
        Returns absolute direction for stairs by relative according current gaze direction
        :param direction:
        :return:
        """
        return Relative.mapping_stair[self.direction][direction]

    def get_torch_abs_direction(self, direction: int) -> int:
        """
        Returns absolute direction for torches by relative according current gaze direction
        :param direction:
        :return:
        """
        return Relative.mapping_torch[self.direction][direction]