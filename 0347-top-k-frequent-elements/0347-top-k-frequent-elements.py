class Solution:

	def topKFrequent(self,nums,K):

		counts, maxCount, result = {}, 0, []

		for num in nums:

			counts[num] = counts.get(num,0) + 1

			maxCount = max(maxCount,counts[num])

		buckets = [[] for _ in range(maxCount+1)]

		for num,count in counts.items():

			buckets[count].append(num)

		for index in range(len(buckets)-1,-1,-1):

			currBucket = buckets[index]

			for num in currBucket:

				result.append(num)

				K-=1

				if K == 0:

					return result

		