class Solution:

	def maxArea(self, heights):

		firstLine, secondLine = 0, len(heights)-1

		resultArea = 0

		while firstLine < secondLine:

			currentArea = (secondLine - firstLine) * min(heights[firstLine], heights[secondLine])

			resultArea = max(resultArea, currentArea)

			if heights[firstLine] < heights[secondLine]:

				firstLine += 1

			else:

				secondLine -= 1

		return resultArea