class Solution:

	def trap(self,heights):

		left, right = 0, len(heights)-1

		maxLeft, maxRight, result = heights[left], heights[right], 0

		while left < right:

			if maxLeft <= maxRight:

				left += 1

				maxLeft = max(maxLeft,heights[left])

				result += maxLeft - heights[left]

			else:

				right -= 1

				maxRight = max(maxRight,heights[right])

				result += maxRight - heights[right]

		return result


		