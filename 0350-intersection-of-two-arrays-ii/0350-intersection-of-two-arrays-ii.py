class Solution:

	def intersect(self, firstList, secondList):

		if len(firstList) > len(secondList):

			return self.intersect(secondList, firstList)

		result = []

		counts = {}

		for num in firstList:

			counts[num] = counts.get(num,0) + 1

		for num in secondList:

			if counts.get(num,0) > 0:

				result.append(num)

				counts[num] -= 1
	
		return result
