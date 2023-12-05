class Solution:

	def minCostClimbingStairs(self,cost):

		targetStep = len(cost)

		return min(self.calculateMinCost(cost,targetStep-1,{}),self.calculateMinCost(cost,targetStep-2,{}))

	def calculateMinCost(self,cost,currStep,cache):

		if currStep <= 1:

			return cost[currStep]

		if currStep in cache:

			return cache[currStep]

		cache[currStep] = cost[currStep] + min(self.calculateMinCost(cost,currStep-1,cache),self.calculateMinCost(cost,currStep-2,cache))

		return cache[currStep]



		