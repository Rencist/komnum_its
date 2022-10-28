import math

class Trapezoida:
    def __init__(self, func, bottomBound:float = 1, topBound:float = 3):
        self.func = func
        self.bottomBound = bottomBound
        self.topBound = topBound
        self.boundOne = 1/math.sqrt(3)
        self.data = {}

    def computeIntegration(self, section:int) -> float:
        tpb = (self.topBound + self.bottomBound) / 2
        tmb = (self.topBound - self.bottomBound) / 2
        x0 = tpb - (tmb * self.boundOne)
        x1 = tpb + (tmb * self.boundOne)

        result = (self.func(x0) * tmb) + (self.func(x0) * tmb)
        return result

