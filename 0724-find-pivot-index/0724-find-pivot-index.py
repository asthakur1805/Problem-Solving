class Solution:

	def pivotIndex(self,nums):

		total = 0

		for num in nums:

			total += num

		leftSum = 0

		for currIndex, currNum in enumerate(nums):

			rightSum = total - currNum - leftSum

			if rightSum == leftSum: return currIndex

			leftSum += currNum

		return -1