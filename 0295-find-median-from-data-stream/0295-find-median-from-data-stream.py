from heapq import heapify, heappush, heappop

class MedianFinder:

	def __init__(self):

		self.smallHeap, self.largeHeap = [], []

		heapify(self.smallHeap)
		heapify(self.largeHeap)

	def addNum(self,num):

		if num >= (self.largeHeap[0] if len(self.largeHeap) > 0 else float('inf')):

			heappush(self.largeHeap,num)

			if len(self.largeHeap) > len(self.smallHeap)+1:

				heappush(self.smallHeap,-heappop(self.largeHeap))

		else:

			heappush(self.smallHeap,-num)

			if len(self.smallHeap) > len(self.largeHeap)+1:

				heappush(self.largeHeap,-heappop(self.smallHeap))

	def findMedian(self):

		numElements = len(self.smallHeap)+len(self.largeHeap)

		if numElements % 2:

			if len(self.smallHeap) == len(self.largeHeap) + 1:

				return -self.smallHeap[0]

			return self.largeHeap[0]

		return (-self.smallHeap[0] + self.largeHeap[0]) / 2

		