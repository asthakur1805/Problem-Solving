from heapq import heapify

class Solution:

	def topKFrequent(self,nums,K):

		counts, result = {}, []

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		maxHeap = [(-count,num) for num,count in counts.items()]

		heapify(maxHeap)

		for _ in range(K):

			result.append(heappop(maxHeap)[1])

		return result