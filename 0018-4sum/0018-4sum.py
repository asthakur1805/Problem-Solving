class Solution:

	def fourSum(self, nums, target):

		nums.sort()

		result = []

		for firstIndex, firstValue in enumerate(nums):

			if firstIndex > 0 and nums[firstIndex-1] == firstValue:

				continue

			for secondIndex in range(firstIndex + 1, len(nums)):

				if secondIndex > firstIndex+1 and nums[secondIndex-1] == nums[secondIndex]:

					continue

				thirdIndex, fourthIndex = secondIndex + 1, len(nums)-1

				while thirdIndex < fourthIndex:

					addition = firstValue + nums[secondIndex] + nums[thirdIndex] + nums[fourthIndex]

					if addition < target:

						thirdIndex += 1

					elif addition > target:

						fourthIndex -= 1

					else:

						result.append([firstValue, nums[secondIndex], nums[thirdIndex], nums[fourthIndex]])

						thirdIndex += 1

						while thirdIndex < fourthIndex and nums[thirdIndex] == nums[thirdIndex-1]:

							thirdIndex += 1


		return result