class Solution:

	def nextGreaterElement(self,firstArr,secondArr):

		numsMap = {value:index for index,value in enumerate(firstArr)}

		stack = []

		result = [-1] * len(firstArr)

		for num in secondArr:

			while stack and num > stack[-1]:

				updateIndex = numsMap[stack.pop()]

				result[updateIndex] = num

			if num in numsMap:

				stack.append(num)

		return result