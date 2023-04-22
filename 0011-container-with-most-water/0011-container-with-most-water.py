class Solution:

	def maxArea(self, heights):

		resultArea = 0

		left, right = 0, len(heights)-1

		while left < right:

			resultArea = max(resultArea, (right-left) * min(heights[left], heights[right]))

			if heights[left] < heights[right]:

				left += 1

			else:

				right -= 1

		return resultArea
		