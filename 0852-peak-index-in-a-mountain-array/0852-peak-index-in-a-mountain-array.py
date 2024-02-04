class Solution:

	def peakIndexInMountainArray(self,nums):

		for index in range(1,len(nums)-1):

			if nums[index-1] < nums[index] > nums[index+1]:

				return index