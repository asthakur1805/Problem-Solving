class Solution:

	def trap(self,heights):

		maxLeft = [0]*len(heights)

		currMax = 0

		for index in range(len(heights)):

			maxLeft[index] = currMax
			currMax = max(currMax,heights[index])

		currMax, result = 0, 0

		for index in range(len(heights)-1,-1,-1):

			result += max(0,min(maxLeft[index],currMax)-heights[index])
			currMax = max(currMax,heights[index])

		return result

			


			