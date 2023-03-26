class Solution:

	def rotate(self, nums, numRotations):

		numRotations %= len(nums)

		self.reverseHelper(nums, 0, len(nums)-1)

		self.reverseHelper(nums, 0, numRotations-1)

		self.reverseHelper(nums, numRotations, len(nums)-1)

	def reverseHelper(self, nums, leftPointer, rightPointer):

		while leftPointer < rightPointer:

			nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
			leftPointer += 1
			rightPointer -= 1

		