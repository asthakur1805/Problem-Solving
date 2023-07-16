class Solution:

	def findKthLargest(self, nums, K):

		nums.sort()
		
		return nums[len(nums)-K]