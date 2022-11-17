class Solution:

	def nextPermutation(self, nums):

		numsLength = len(nums)

		prefixIndex = -1

		for currIndex in range(numsLength-2,-1,-1):

			if nums[currIndex] < nums[currIndex + 1]:

				prefixIndex = currIndex
				break

		if prefixIndex >= 0:

			for suffixIndex in range(numsLength-1,-1,-1):

				if nums[suffixIndex] > nums[prefixIndex]:

					nums[prefixIndex], nums[suffixIndex] = nums[suffixIndex], nums[prefixIndex]

					break

		leftPointer, rightPointer = prefixIndex + 1, numsLength - 1

		while leftPointer < rightPointer:

			nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
			leftPointer, rightPointer = leftPointer + 1, rightPointer - 1