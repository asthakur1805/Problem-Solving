class Solution:

	def minCostClimbingStairs(self, cost):

		first, second = cost[-1], 0

		for index in range(len(cost)-2,-1,-1):

			temp = first
			first = cost[index] + min(first,second)
			second = temp

		return min(first,second)