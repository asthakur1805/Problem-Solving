class Solution:

	def largestRectangleArea(self,heights):

		stack, result = [], 0

		for currIndex, currHeight in enumerate(heights):

			while stack and currHeight < heights[stack[-1]]:

				nextSmaller = currIndex
				prevSmaller = stack[-2] if len(stack)>1 else -1

				result = max(result,(nextSmaller-prevSmaller-1)*heights[stack[-1]])

				stack.pop()

			stack.append(currIndex)

		nextSmaller = len(heights)

		while stack:

			prevSmaller = stack[-2] if len(stack)>1 else -1

			result = max(result,(nextSmaller-prevSmaller-1)*heights[stack[-1]])

			stack.pop()

		return result