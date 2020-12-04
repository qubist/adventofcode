import sys, time
sys.path.append('../')

from list import *

POSITION_DIGITS = 5
VELOCITY_DIGITS = 1

RESONABLE_RANGE = 800

positionLength = 1+POSITION_DIGITS+2+1+POSITION_DIGITS # sign + number + comma + space & sign + number
velocityLength = 1+VELOCITY_DIGITS+2+1+VELOCITY_DIGITS

class RescuePoint:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return str(self.position) + ' ' + str(self.velocity)

    def move(self):
        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]

class PointsList(List):
    def __init__(self, file):
        super().__init__(file)
        self.range = ()
        self.numElements = 0
        self.canvas = [[]]

        self.load()
        for line in self.data:
            position = line[10:10+positionLength]
            velocity = line[10+positionLength+12:10+positionLength+12+velocityLength]
            #print(position)
            pX = int(position[:1+POSITION_DIGITS])
            pY = int(position[1+POSITION_DIGITS+2:])
            #print(pX)
            #print(pY)
            #print(velocity)
            vX = int(velocity[:1+VELOCITY_DIGITS])
            vY = int(velocity[1+VELOCITY_DIGITS+2:])
            #print(vX)
            #print(vY)

            self.list.append(RescuePoint([pX,pY],[vX,vY]))

        self.numElements = len(self.list)

        # calculate range
        self.range = self.calculateRange()

    def setUpCanvas(self):
        # set up canvas of empty string with a big enough size for all points
        size = self.range[1]+2
        # self.canvas = [['' for x in range(1400)] for y in range(275)]
        print("SETTING UP CANVAS!")
        self.canvas = [['' for x in range(75)] for y in range(75)]
        print("DONE!")

    # returns the range of the points list in their current positions
    def calculateRange(self):
        positions = []
        for point in self.list:
            positions.append(point.position[0])
            positions.append(point.position[1])
        return ((min(positions), max(positions)), max(positions) - min(positions))

    # adds the minimum value's magnitude to each coordinate so everything is positive
    def makePositive(self):
        for point in self.list:
            point.position[0] += abs(self.range[0][0])
            point.position[1] += abs(self.range[0][0])

        # recalculate range:
        self.range = self.calculateRange()

    # subtracts the minimum value's magnitude from each coordinate so the values
    # are always "zeroed" near the origin
    def zero(self):
        for point in self.list:
            point.position[0] -= abs(self.range[0][0]) - 1
            point.position[1] -= abs(self.range[0][0]) - 1
        # recalculate range:
        self.range = self.calculateRange()

    # simply applies move() to all points in the point list
    def moveAll(self):
        for point in self.list:
            x = point.position[0]
            y = point.position[1]

            # reset trail on canvas if it's set up
            if self.canvas != [[]]:
                try: self.canvas[y][x] = ''
                except: pass

            point.move()
        self.zero()
        self.range = self.calculateRange()
        if self.range[1] < RESONABLE_RANGE and self.canvas == [[]]:
            self.setUpCanvas()

    def animate(self):
        seconds = 0
        while True:
            print(self.range)
            self.moveAll()
            seconds += 1
            print(f'Seconds elapsed: {seconds}')
            if self.range[1] < RESONABLE_RANGE: time.sleep(.1)
            if self.range[1] < RESONABLE_RANGE/10: time.sleep(.7)
            if self.range[1] == 61:
                print("SMALLEST POINT FOUND")
                print(self)
                print(f'Seconds: {seconds}')

    def __str__(self):
        # add points to the canvas as #
        # FORMAT REMINDER: canvas[y][x]
        for point in self.list:
            x = point.position[0]
            y = point.position[1]
            assert x >= 0
            assert y >= 0
            try: self.canvas[y][x] = '#'
            except: pass
        # return the canvas one letter and line at a time, in order
        out = ''
        for y in self.canvas:
            for x in y:
                if x == '':
                    out += '.'
                else:
                    out += x
            out += '\n'
        return out

if __name__ == '__main__':
    # l = PointsList("testInput.txt")
    l = PointsList("input.txt")
    l.makePositive()
    l.animate()
