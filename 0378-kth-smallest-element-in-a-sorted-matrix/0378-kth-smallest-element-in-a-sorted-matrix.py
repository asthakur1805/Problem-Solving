from heapq import heappush, heappop

class Solution:

	def kthSmallest(self,matrix,K):

		minHeap = []

		for row in range(min(K,len(matrix))):

			heappush(minHeap,(matrix[row][0],row,0))

		for _ in range(K-1):

			_, currRow, currColumn = heappop(minHeap)

			if currColumn + 1 < len(matrix):

				heappush(minHeap,(matrix[currRow][currColumn+1],currRow,currColumn+1))

		return minHeap[0][0]

