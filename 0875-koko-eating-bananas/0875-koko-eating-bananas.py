class Solution:

	def minEatingSpeed(self,piles,allowedHours):

		maxSpeed = max(piles)

		left, right = 1, maxSpeed

		while left <= right:

			mid = left + (right - left) // 2

			totalHours = 0

			for pile in piles:

				totalHours += ceil(pile/mid)

			if totalHours <= allowedHours:

				result = mid
				right = mid - 1

			else:

				left = mid + 1

		return result



