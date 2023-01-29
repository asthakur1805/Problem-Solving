class Solution:

	def rotate(self, nums, numRotations):

		numRotations %= len(nums)

		self.reverse(nums, 0, len(nums)-1)

		self.reverse(nums, 0, numRotations-1)

		self.reverse(nums, numRotations, len(nums)-1)

	def reverse(self, nums, leftPointer, rightPointer):

		while leftPointer < rightPointer:

			nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]

			leftPointer, rightPointer = leftPointer + 1, rightPointer - 1


