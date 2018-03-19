# Globals for the bearings
# Change the values as you see fit
EAST = 3
NORTH = 2
WEST = 1
SOUTH = 0

# Installing PyPatt for Pattern matching
# pip install pypatt
import pypatt

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing += 1
        if self.bearing > 3:
            self.bearing = 0

    def turn_left(self):
        self.bearing -= 1
        if self.bearing < 0:
            self.bearing = 3

    @pypatt.transform
    def advance(self):
        with match(self.bearing):
            with EAST:
                self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
            with NORTH:
                self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
            with WEST:
                self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
            with SOUTH:
                self.coordinates = (self.coordinates[0], self.coordinates[1]-1)

    @pypatt.transform
    def simulate(self, directions=''):
        for direc in directions:
            with match(direc):
                with 'L':
                    self.turn_left()
                with 'R':
                    self.turn_right()
                with 'A':
                    self.advance()

