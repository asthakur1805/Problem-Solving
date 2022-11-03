class Solution:

	def threeSum(self, nums):

		nums.sort()

		result = []

		for firstIndex, firstNumber in enumerate(nums):

			if firstIndex > 0 and firstNumber == nums[firstIndex-1]:

				continue

			secondIndex, thirdIndex = firstIndex+1, len(nums)-1

			while secondIndex < thirdIndex:

				addition = firstNumber + nums[secondIndex] + nums[thirdIndex]

				if addition < 0:

					secondIndex += 1

				elif addition > 0:

					thirdIndex -= 1

				else:

					result.append([firstNumber, nums[secondIndex], nums[thirdIndex]])
		
					secondIndex += 1

					while secondIndex < thirdIndex and nums[secondIndex] == nums[secondIndex-1]:

						secondIndex += 1


		return result

			