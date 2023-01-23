class Solution:

	def rotate(self, nums, rotations):

		numsLength = len(nums)

		rotations %= numsLength

		self.reverse(nums, 0, numsLength - 1)

		self.reverse(nums, 0, rotations-1)

		self.reverse(nums, rotations, numsLength-1)
		
	def reverse(self, nums, leftPointer, rightPointer):

		while leftPointer < rightPointer:

			nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]

			leftPointer, rightPointer = leftPointer + 1 , rightPointer - 1

	