class Solution:

	def canCompleteCircuit(self,gas,cost):

		sumGas, sumCost = 0, 0

		for index in range(len(gas)):

			sumGas += gas[index]
			sumCost += cost[index]

		if sumGas < sumCost:

			return -1

		startIndex, currIndex = 0, 0

		while startIndex < len(gas):

			totalGas = 0

			for currIndex in range(startIndex,len(gas)):

				totalGas += (gas[currIndex]-cost[currIndex])

				if totalGas < 0:

					break

			else:

				return startIndex

			startIndex = currIndex+1

		

				