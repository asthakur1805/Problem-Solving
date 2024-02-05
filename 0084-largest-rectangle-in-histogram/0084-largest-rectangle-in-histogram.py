class Solution:

	def largestRectangleArea(self,heights):

		stack = []

		rightSmaller = [len(heights)]*len(heights)

		for currIndex in range(len(heights)):

			while stack and heights[currIndex] < heights[stack[-1]]:

				rightSmaller[stack.pop()] = currIndex

			stack.append(currIndex)

		while stack:

			stack.pop()

		leftSmaller = [-1]*len(heights)
		
		for currIndex in range(len(heights)-1,-1,-1):

			while stack and heights[currIndex] < heights[stack[-1]]:

				leftSmaller[stack.pop()] = currIndex

			stack.append(currIndex)

		result = 0

		for currIndex in range(len(heights)):

			result = max(result,(rightSmaller[currIndex]-leftSmaller[currIndex]-1)*heights[currIndex])

		return result
