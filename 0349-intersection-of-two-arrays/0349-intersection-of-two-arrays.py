class Solution:

	def intersection(self, smallArr, largeArr):

		if len(smallArr) > len(largeArr):

			return self.intersection(largeArr, smallArr)

		numsSet = set()

		intersectSet = set()

		for num in smallArr:

			numsSet.add(num)

		for num in largeArr:

			if num in numsSet:

				intersectSet.add(num)

		return list(intersectSet)
		