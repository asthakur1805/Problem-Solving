class Solution:

	def dailyTemperatures(self, temperatures):

		result = [0] * len(temperatures)

		stack = []

		for currIndex, temperature in enumerate(temperatures):

			while stack and temperature > temperatures[stack[-1]]:

				oldIndex = stack.pop()
				result[oldIndex] = currIndex - oldIndex

			stack.append(currIndex)

		while stack:

			result[stack.pop()] = 0

		return result