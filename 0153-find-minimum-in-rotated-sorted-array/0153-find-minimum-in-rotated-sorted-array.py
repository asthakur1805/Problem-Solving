class Solution:

	def findMin(self, nums):

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if leftPointer == rightPointer or nums[midPointer] > nums[midPointer+1]:
	
				pivotIndex = midPointer
				break

			if nums[0] <= nums[midPointer]:

				leftPointer = midPointer + 1

			else:

				rightPointer = midPointer - 1

		if pivotIndex == len(nums)-1:
				return nums[0]

		return nums[pivotIndex+1]
