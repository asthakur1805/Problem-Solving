from heapq import heapify, heappop

class Solution:

	def kClosest(self, points, K):

		minHeap = [(x*x+y*y,[x,y]) for [x,y] in points]

		heapify(minHeap)

		result = []

		for _ in range(K):

			result.append(heappop(minHeap)[1])

		return result