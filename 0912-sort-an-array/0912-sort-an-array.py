class Solution:

	def sortArray(self, nums):

		self.mergeSort(nums, 0, len(nums)-1)

		return nums

	def mergeSort(self, nums, leftPointer, rightPointer):

		if leftPointer >= rightPointer:

			return

		midPointer = leftPointer + (rightPointer-leftPointer) // 2

		self.mergeSort(nums, leftPointer, midPointer)

		self.mergeSort(nums, midPointer+1, rightPointer)

		self.merge(nums, leftPointer, midPointer, rightPointer)

	def merge(self, nums, leftPointer, midPointer, rightPointer):

		leftSubArray, rightSubArray = nums[leftPointer:midPointer+1], nums[midPointer+1:rightPointer+1]

		firstIndex, secondIndex, resultIndex = 0, 0, leftPointer

		while firstIndex < len(leftSubArray) and secondIndex < len(rightSubArray):

			if leftSubArray[firstIndex] <= rightSubArray[secondIndex]:

				nums[resultIndex] = leftSubArray[firstIndex]
				firstIndex += 1

			else:

				nums[resultIndex] = rightSubArray[secondIndex]
				secondIndex += 1

			resultIndex += 1

		while firstIndex < len(leftSubArray):

			nums[resultIndex] = leftSubArray[firstIndex]
			firstIndex += 1
			resultIndex += 1

		while secondIndex < len(rightSubArray):

			nums[resultIndex] = rightSubArray[secondIndex]
			secondIndex += 1
			resultIndex += 1


				

				
		
		