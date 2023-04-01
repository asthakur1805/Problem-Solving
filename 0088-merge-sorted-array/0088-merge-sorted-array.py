class Solution:

	def merge(self, firstArr, firstLength, secondArr, secondLength):

		firstIndex, secondIndex, resultIndex = firstLength-1, secondLength-1, firstLength+secondLength-1

		while firstIndex >= 0 and secondIndex >= 0:

			if firstArr[firstIndex] > secondArr[secondIndex]:

				firstArr[resultIndex] = firstArr[firstIndex]
				firstIndex -= 1

			else:

				firstArr[resultIndex] = secondArr[secondIndex]
				secondIndex -= 1

			resultIndex -= 1

		while secondIndex >= 0:

			firstArr[resultIndex] = secondArr[secondIndex]
			resultIndex -= 1
			secondIndex -= 1

