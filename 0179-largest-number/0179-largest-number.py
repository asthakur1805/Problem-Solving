class Solution:

	def largestNumber(self,nums):

		hasOnlyZeroes = True

		for index, num in enumerate(nums):

			if num != 0:

				hasOnlyZeroes = False

			nums[index] = str(num)

		if hasOnlyZeroes:

			return "0"

		self.quickSort(nums,0,len(nums)-1)

		return ''.join(nums)

	def quickSort(self,nums,left,pivot):

		if left >= pivot:

			return

		partition = left

		for curr in range(left,pivot):

			if self.compare(nums[curr],nums[pivot]) == -1:

				nums[partition], nums[curr] = nums[curr], nums[partition]
				partition += 1

		nums[partition], nums[pivot] = nums[pivot], nums[partition]
        
		self.quickSort(nums,left,partition-1)

		self.quickSort(nums,partition+1,pivot)

	def compare(self,firstNum,secondNum):

		return -1 if firstNum+secondNum > secondNum+firstNum else 1
		
				

		

	