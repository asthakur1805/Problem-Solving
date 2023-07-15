from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:

	def __init__(self, K, nums):

		self.minHeap, self.K = nums, K

		heapify(self.minHeap)

		while len(self.minHeap) > self.K:

			heappop(self.minHeap)

	def add(self, element):

		if len(self.minHeap) < self.K:

			heappush(self.minHeap, element)

		else:

			heappushpop(self.minHeap, element)

		return self.minHeap[0]

		