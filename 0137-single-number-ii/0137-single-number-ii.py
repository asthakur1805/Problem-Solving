class Solution:

	def singleNumber(self, nums):

		if len(nums) == 1:

			return nums[0]

		nums.sort()

		if nums[-1] > nums[-2]:

			return nums[-1]

		for index in range(1,len(nums),3):

			if nums[index-1] != nums[index]:

				return nums[index-1]
