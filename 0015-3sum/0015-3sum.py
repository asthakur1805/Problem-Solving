class Solution:

	def threeSum(self, nums):

		nums.sort()

		result, numsLength = [], len(nums)

		for firstIndex in range(numsLength):

			firstNumber = nums[firstIndex]

			if firstIndex > 0 and nums[firstIndex-1] == firstNumber:

				continue

			secondIndex, thirdIndex = firstIndex + 1, numsLength - 1

			while secondIndex < thirdIndex:

				secondNumber, thirdNumber = nums[secondIndex], nums[thirdIndex]

				addition = firstNumber + secondNumber + thirdNumber

				if addition < 0:

					secondIndex += 1

				elif addition > 0:

					thirdIndex -= 1

				else:

					result.append([firstNumber, secondNumber, thirdNumber])

					secondIndex += 1

					while secondIndex < thirdIndex and nums[secondIndex] == nums[secondIndex-1]:

						secondIndex += 1


		return result
			

				

			