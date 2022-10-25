class Solution:

	def search(self, nums, target):

		if not nums:
			return -1

		leftPointer, rightPointer = 0, len(nums)-1

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if leftPointer == rightPointer or nums[midPointer] > nums[midPointer+1]:
				
				pivotIndex = midPointer
				break

			if nums[leftPointer] <= nums[midPointer]:

				leftPointer = midPointer + 1

			else:
		
				rightPointer = midPointer - 1

		if nums[0] <= target <= nums[pivotIndex]:

			return self.binarySearch(nums, target, 0, pivotIndex)

		return self.binarySearch(nums, target, pivotIndex+1, len(nums)-1)


		
	def binarySearch(self, nums, target, leftPointer, rightPointer):

		while leftPointer <= rightPointer:

			midPointer = leftPointer + (rightPointer - leftPointer) // 2

			if nums[midPointer] == target:
				return midPointer

			if target < nums[midPointer]:

				rightPointer = midPointer - 1

			else:

				leftPointer = midPointer + 1

		return -1
				