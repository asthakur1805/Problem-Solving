class Solution:

	def rotate(self, nums, numRotations):

		numRotations %= len(nums)

		self.reverse(nums, 0, len(nums)-1)

		self.reverse(nums, 0, numRotations-1)

		self.reverse(nums, numRotations, len(nums)-1)

	def reverse(self, nums, left, right):

		while left < right:

			nums[left], nums[right] = nums[right], nums[left]
			left += 1
			right -= 1

	

