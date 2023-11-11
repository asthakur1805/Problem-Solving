class Solution:

	def topKFrequent(self,nums,K):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		sortedCounts = sorted([(count,num) for num,count in counts.items()],reverse=True)

		return [sortedCounts[index][1] for index in range(K)]