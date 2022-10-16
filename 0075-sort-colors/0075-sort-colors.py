class Solution:

	def sortColors(self, nums):

		leftPointer = midPointer = 0
		
		rightPointer = len(nums)-1

		while midPointer <= rightPointer:

			if nums[midPointer] == 0:

				nums[midPointer], nums[leftPointer] = nums[leftPointer], nums[midPointer]

				midPointer += 1
			
				leftPointer += 1

			elif nums[midPointer] == 1:

				midPointer += 1

			else:

				nums[midPointer], nums[rightPointer] = nums[rightPointer], nums[midPointer]

				rightPointer -= 1