class Solution:

	def shipWithinDays(self,weights,maxDays):

		left, right = float(-inf), 0

		for weight in weights:

			left = max(left,weight)
			right += weight

		while left <= right:

			mid = left + (right-left) // 2

			if self.calculateDaysToShip(weights,mid) > maxDays:

				left = mid + 1

			else:

				result = mid
				right = mid - 1

		return result

	def calculateDaysToShip(self,weights,capacity):

		totalWeight, result = 0, 1

		for currWeight in weights:

			if totalWeight + currWeight > capacity:

				result += 1
				totalWeight = currWeight

			else:
				
				totalWeight += currWeight

		return result

			
		
		