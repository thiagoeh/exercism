# Globals for the bearings
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self._x = x
        self._y = y

    @property
    def coordinates(self):
        """
        Coordinates tuple (x, y)
        """
        return (self._x, self._y)

    def advance(self):
        """
        Based on bearing, advance one coordinate point
        """
        if self.bearing == EAST:
            self._x += 1
        elif self.bearing == WEST:
            self._x -= 1
        elif self.bearing == NORTH:
            self._y += 1
        elif self.bearing == SOUTH:
            self._y -= 1

    def turn_left(self):
        """
        Change bearing to the left
        """
        if self.bearing == EAST:
            self.bearing = NORTH
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == SOUTH:
            self.bearing = EAST

    def turn_right(self):
        """
        Change bearing to the right
        """
        if self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == WEST:
            self.bearing = NORTH
        elif self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == SOUTH:
            self.bearing = WEST

    def simulate(self, sequence):
        """
        Apply a sequence of commands in the format turn (R)ight/(L)eft and (A)dvance
        """
        for c in sequence:
            if c == 'R':
                self.turn_right()
            elif c == 'L':
                self.turn_left()
            elif c == 'A':
                self.advance()
