class Solution:

	def maximalRectangle(self,matrix):

		result = float('-inf')

		heights = [0]*len(matrix[0])

		for row in range(len(matrix)):

			for column in range(len(matrix[0])):

				if matrix[row][column] == '1':

					heights[column] += 1

				else:

					heights[column] = 0

			result = max(result,self.largestRectangleArea(heights))

		return result
		

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