class Solution:

	def threeSumClosest(self, nums, target):

		nums.sort()

		absDifference = float('inf')

		result = 0

		for firstIndex, firstValue in enumerate(nums):

			secondIndex, thirdIndex = firstIndex + 1, len(nums) - 1

			while secondIndex < thirdIndex:

				secondValue, thirdValue = nums[secondIndex], nums[thirdIndex]

				numberSum = firstValue + secondValue + thirdValue

				if abs(numberSum - target) < absDifference:

					absDifference = abs(numberSum - target)
					result = numberSum

				if numberSum < target:

					secondIndex += 1

				else:
	
					thirdIndex -= 1


		return result


			