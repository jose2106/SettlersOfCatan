from time import time
class Generator:
    def __init__(self, a = 5, c = 7, m = 8, low = None, high = None, rounded = False):
        self.X = int(time()) # seed
        self.a = a
        self.c = c
        self.m = m
        self.low = low
        self.high = high
        self.rounded = rounded
        self.span = None
        if self.low is not None and self.high is not None:
            self.span = self.high - self.low

    def throw(self):
        self.X = (self.a * self.X + self.c) % self.m
        result = self.X
        if self.span is not None:
            result /= self.m - 1 # values from 0 to m, originally, now from 0 to 1
            result *= self.span # make that 0 to high - low
            result += self.low # and then from low to high
        if self.rounded:
            return round(result) # round if requested
        else:
            return result
