class Solution:

	def largestRectangleArea(self,heights):

		stack, result = [], 0

		for currIndex in range(len(heights)+1):

			while stack and (currIndex == len(heights) or heights[currIndex] < heights[stack[-1]]):

				nextSmaller = currIndex 
				prevSmaller = stack[-2] if len(stack)>1 else -1

				result = max(result,(nextSmaller-prevSmaller-1)*heights[stack[-1]])

				stack.pop()

			stack.append(currIndex)

		return result
