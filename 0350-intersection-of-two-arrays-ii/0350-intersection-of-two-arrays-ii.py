class Solution:

	def intersect(self, smallArr, largeArr):

		if len(largeArr) < len(smallArr):

			return self.intersect(largeArr, smallArr)

		counts = {}

		for num in smallArr:

			counts[num] = counts.get(num, 0) + 1

		result = []

		for num in largeArr:

			if counts.get(num, 0) > 0:

				result.append(num)

				counts[num] -= 1

		return result