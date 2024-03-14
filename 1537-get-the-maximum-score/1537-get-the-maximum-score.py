class Solution:

	def maxSum(self,firstArr,secondArr):

		mod = (10**9+7)

		firstIndex, secondIndex = 0, 0

		firstResult, secondResult = 0, 0

		while firstIndex < len(firstArr) or secondIndex < len(secondArr):

			if firstIndex < len(firstArr) and (secondIndex == len(secondArr) or firstArr[firstIndex] < secondArr[secondIndex]):

				firstResult += firstArr[firstIndex]
				firstIndex += 1

			elif secondIndex < len(secondArr) and (firstIndex == len(firstArr) or secondArr[secondIndex] < firstArr[firstIndex]):

				secondResult += secondArr[secondIndex]
				secondIndex += 1

			else:

				firstResult = secondResult = max(firstResult,secondResult) + firstArr[firstIndex]
				firstIndex += 1
				secondIndex += 1

		return max(firstResult,secondResult) % mod