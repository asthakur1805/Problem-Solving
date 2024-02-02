class Solution:

	def majorityElement(self,nums):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		result = []

		for num,count in counts.items():

			if count > len(nums) // 3:

				result.append(num)

			if len(result) == 2:

				break

		return result
		
			