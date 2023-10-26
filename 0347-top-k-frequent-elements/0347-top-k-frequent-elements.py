class Solution:

	def topKFrequent(self,nums,K):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		sortedCounts = sorted([item for item in counts.items()],key=lambda count:count[1],reverse=True)

		return [sortedCounts[index][0] for index in range(K)]