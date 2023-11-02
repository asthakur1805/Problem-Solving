from heapq import heapify, heappop

class Solution:

	def kClosest(self,points,K):

		minHeap = [(x**2+y**2,[x,y]) for [x,y] in points]

		heapify(minHeap)

		return [heappop(minHeap)[1] for _ in range(K)]
