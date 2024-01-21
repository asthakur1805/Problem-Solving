class Solution:

	def nextGreaterElement(self,firstArr,secondArr):

		numsMap = {num:index for index,num in enumerate(firstArr)}

		stack = []

		result = [-1] * len(firstArr)

		for currNum in secondArr:

			while stack and currNum > stack[-1]:

				updateIndex = numsMap[stack.pop()]

				result[updateIndex] = currNum

			if currNum in numsMap:

				stack.append(currNum)

		return result
		