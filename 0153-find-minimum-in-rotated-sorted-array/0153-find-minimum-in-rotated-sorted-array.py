class Solution:

	def findMin(self, nums):

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if leftPointer == rightPointer or nums[midPointer] > nums[midPointer + 1]:

				pivotIndex = midPointer
				break

			if nums[leftPointer] <= nums[midPointer]:

				leftPointer = midPointer + 1

			else:

				rightPointer = midPointer - 1


		result = nums[0] if pivotIndex == len(nums)-1 else nums[pivotIndex + 1]

		return result