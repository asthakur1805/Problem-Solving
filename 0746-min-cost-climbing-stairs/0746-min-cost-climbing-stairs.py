class Solution:

	def minCostClimbingStairs(self,cost):

		first, second = cost[0], cost[1]

		for index in range(2,len(cost)):

			first, second = second, cost[index] + min(first,second)

		return min(first,second)