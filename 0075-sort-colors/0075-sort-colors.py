class Solution:

	def sortColors(self, nums):

		leftPointer, midPointer, rightPointer = 0, 0, len(nums)-1

		while midPointer <= rightPointer:

			if nums[midPointer] == 0:

				nums[leftPointer], nums[midPointer] = nums[midPointer], nums[leftPointer]
				midPointer += 1
				leftPointer += 1

			elif nums[midPointer] == 1:

				midPointer += 1

			else:

				nums[midPointer], nums[rightPointer] = nums[rightPointer], nums[midPointer]
				rightPointer -= 1

		
		