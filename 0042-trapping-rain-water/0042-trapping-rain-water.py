class Solution:

	def trap(self, heights):

		result = 0

		maxLeft, maxRight, currLeft, currRight = [0]*len(heights), [0]*len(heights), 0, 0

		for index in range(len(heights)):

			maxLeft[index] = currLeft
			currLeft = max(currLeft, heights[index])

		for index in range(len(heights)-1,-1,-1):

			maxRight[index] = currRight
			currRight = max(currRight, heights[index])

			result += max(min(maxLeft[index], maxRight[index]) - heights[index], 0)

		return result