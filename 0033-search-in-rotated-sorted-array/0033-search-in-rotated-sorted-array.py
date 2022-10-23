class Solution:

	def search(self, nums, target):

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if nums[midPointer] == target:

				return midPointer

			if nums[leftPointer] <= nums[midPointer]:

				if nums[leftPointer] <= target <= nums[midPointer]:

					rightPointer = midPointer - 1

				else:

					leftPointer = midPointer + 1

			else:

				if nums[midPointer] <= target <= nums[rightPointer]:

					leftPointer = midPointer + 1

				else:

					rightPointer = midPointer - 1

		return -1