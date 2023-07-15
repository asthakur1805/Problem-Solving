class Solution:

	def topKFrequent(self, nums, K):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		sortedCounts = sorted(counts.items(), reverse=True, key=lambda x:x[1])

		return [sortedCounts[index][0] for index in range(K)]