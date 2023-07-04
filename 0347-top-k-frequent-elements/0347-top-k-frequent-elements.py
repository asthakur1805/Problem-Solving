class Solution:

	def topKFrequent(self, nums, K):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		result = sorted(counts.items(),reverse=True,key=lambda count:count[1])

		return [result[index][0] for index in range(K)]
		