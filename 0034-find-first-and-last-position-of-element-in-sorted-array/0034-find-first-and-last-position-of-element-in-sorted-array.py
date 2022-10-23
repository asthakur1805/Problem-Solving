class Solution:

	def searchRange(self, nums, target):

		firstIndex = -1

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if nums[midPointer] == target:

				firstIndex = midPointer

				rightPointer = midPointer - 1

			elif target < nums[midPointer]:

				rightPointer = midPointer - 1

			else:

				leftPointer = midPointer + 1

		if firstIndex == -1:

			return [-1, -1]


		leftPointer, rightPointer = firstIndex, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if nums[midPointer] == target:

				lastIndex = midPointer

				leftPointer = midPointer + 1

			elif target < nums[midPointer]:

				rightPointer = midPointer - 1

			else:

				leftPointer = midPointer + 1

		return [firstIndex, lastIndex]
