from heapq import heapify,heappush,heappop,heappushpop

class KthLargest:

	def __init__(self, K, nums):

		self.K, self.minHeap = K, nums

		heapify(self.minHeap)

		while len(self.minHeap) > self.K:

			heappop(self.minHeap)

	def add(self, val):

		if len(self.minHeap) < self.K:

			heappush(self.minHeap, val)

		elif val > self.minHeap[0]:

			heappushpop(self.minHeap, val)

		return self.minHeap[0]