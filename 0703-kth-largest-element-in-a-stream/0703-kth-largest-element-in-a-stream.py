from heapq import heapify, heappush, heappop

class KthLargest:

	def __init__(self,K,nums):

		self.minHeap, self.K = nums, K

		heapify(self.minHeap)

		while len(self.minHeap) > self.K:

			heappop(self.minHeap)

	def add(self,element):

		heappush(self.minHeap,element)

		if len(self.minHeap) > self.K:

			heappop(self.minHeap)

		return self.minHeap[0]