class Solution:

	def findDuplicates(self,nums):

		result = []

		for num in nums:

			num = abs(num)

			if nums[num-1] < 0:

				result.append(num)

			else:

				nums[num-1] *= -1

		return result