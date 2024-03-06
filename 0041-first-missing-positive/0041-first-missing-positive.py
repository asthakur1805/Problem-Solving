class Solution:

	def firstMissingPositive(self,nums):

		for index, num in enumerate(nums):

			if num <= 0:

				nums[index] = len(nums)+1

		for num in nums:

			index = abs(num)-1

			if index < len(nums):

				nums[index] = -abs(nums[index])

		for num in range(1,len(nums)+1):

			index = num-1

			if nums[index] > 0:

				return num

		return len(nums)+1

		