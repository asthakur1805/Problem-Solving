class Solution:

	def intersect(self, firstArr, secondArr):

		firstArr.sort()

		secondArr.sort()

		firstIndex, secondIndex, result = 0, 0, []

		while firstIndex < len(firstArr) and secondIndex < len(secondArr):

			if firstArr[firstIndex] < secondArr[secondIndex]:

				firstIndex += 1

			elif firstArr[firstIndex] > secondArr[secondIndex]:

				secondIndex += 1

			else:
		
				result.append(firstArr[firstIndex])

				firstIndex += 1

				secondIndex += 1

		return result
				