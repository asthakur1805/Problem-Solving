class Solution:

	def dailyTemperatures(self, temperatures):

		stack = []

		result = [0] * len(temperatures)

		for highIndex, currentTemperature in enumerate(temperatures):

			while stack and currentTemperature > temperatures[stack[-1]]:

				lowIndex = stack.pop()
				result[lowIndex] = highIndex - lowIndex

			stack.append(highIndex)

		return result

			
				

		