class Solution:

	def pivotIndex(self,nums):

		arrSum = 0

		for num in nums:

			arrSum += num

		leftSum = 0

		for index, num in enumerate(nums):

			rightSum = arrSum - leftSum - num

			if leftSum == rightSum:

				return index

			leftSum += num

		return -1