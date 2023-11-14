class Solution:

	def sortArray(self,nums):

		self.mergeSort(nums,0,len(nums)-1)

		return nums

	def mergeSort(self,nums,left,right):

		if left >= right:

			return

		mid = left + (right - left) // 2

		self.mergeSort(nums,left,mid)
		
		self.mergeSort(nums,mid+1,right)

		self.merge(nums,left,mid,right)

	def merge(self,nums,left,mid,right):

		firstArr, secondArr = nums[left:mid+1], nums[mid+1:right+1]

		firstIndex, secondIndex, resultIndex = 0, 0, left

		while firstIndex < len(firstArr) and secondIndex < len(secondArr):

			if firstArr[firstIndex] < secondArr[secondIndex]:

				nums[resultIndex] = firstArr[firstIndex]
				firstIndex += 1

			else:

				nums[resultIndex] = secondArr[secondIndex]
				secondIndex += 1

			resultIndex += 1

		while firstIndex < len(firstArr):

			nums[resultIndex] = firstArr[firstIndex]
			firstIndex += 1
			resultIndex += 1

		while secondIndex < len(secondArr):

			nums[resultIndex] = secondArr[secondIndex]
			resultIndex += 1
			secondIndex += 1

	