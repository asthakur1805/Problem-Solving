class Solution:

	def topKFrequent(self, nums, K):

		maxCount, counts = 0, {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

			if counts[num] > maxCount:

				maxCount = counts[num]

		buckets = [[] for _ in range(maxCount+1)]

		for num,count in counts.items():

			buckets[count].append(num)

		result = []

		while True:

			for count in range(maxCount,0,-1):

				bucketNums = buckets[count]

				for num in bucketNums:

					result.append(num)

					K -= 1

					if K == 0:
		
						return result

