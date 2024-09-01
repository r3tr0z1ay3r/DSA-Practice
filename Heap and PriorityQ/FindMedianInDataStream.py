import math


class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            mean = sum(self.arr) / len(self.arr)
            return mean
        else:
            return self.arr[]

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.findMedian()
medianFinder.addNum(3)
medianFinder.findMedian()
medianFinder.addNum(2)
medianFinder.findMedian()