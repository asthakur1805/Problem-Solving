class Solution:

	def trap(self, heights):

		left, right, result = 0, len(heights)-1, 0

		maxLeft, maxRight = heights[left], heights[right]

		while left < right:

			if maxLeft <= maxRight:

				left += 1

				result += max(0, maxLeft-heights[left])

				maxLeft = max(maxLeft, heights[left])

			else:

				right -= 1

				result += max(0, maxRight-heights[right])

				maxRight = max(maxRight, heights[right])

		return result