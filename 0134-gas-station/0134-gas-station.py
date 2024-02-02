class Solution:

	def canCompleteCircuit(self,gas,cost):

		sumGas, sumCost = 0, 0

		for index in range(len(gas)):

			sumGas += gas[index]
			sumCost += cost[index]

		if sumGas < sumCost:

			return -1

		result, totalGas = 0, 0

		for index in range(len(gas)):
				
			totalGas += (gas[index]-cost[index])

			if totalGas < 0:

				result = index + 1
				totalGas = 0

		return result