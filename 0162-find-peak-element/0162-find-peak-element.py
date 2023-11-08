class Solution:

	def findPeakElement(self,nums):

		if len(nums) == 1 or nums[0] > nums[1]:

			return 0

		if nums[len(nums)-1] > nums[len(nums)-2]:

			return len(nums)-1

		for index in range(1,len(nums)-1):

			if nums[index-1] < nums[index] > nums[index+1]:

				return index