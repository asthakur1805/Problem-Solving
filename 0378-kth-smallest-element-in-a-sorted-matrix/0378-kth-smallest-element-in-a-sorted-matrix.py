from heapq import heappush, heappop

class Solution:

	def kthSmallest(self,matrix,K):

		maxHeap = []

		for row in range(len(matrix)):

			for column in range(len(matrix[0])):

				heappush(maxHeap,-matrix[row][column])

				if len(maxHeap) > K:

					heappop(maxHeap)

		return -maxHeap[0]

		