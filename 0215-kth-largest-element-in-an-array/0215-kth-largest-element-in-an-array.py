from heapq import heapify, heappop

class Solution:

	def findKthLargest(self,nums,K):

		maxHeap = [-num for num in nums]

		heapify(maxHeap)

		for _ in range(K):

			result = -heappop(maxHeap)

		return result

		