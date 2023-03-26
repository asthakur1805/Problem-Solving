class Solution:

	def dailyTemperatures(self, temperatures):

		if not temperatures:

			return

		result = [0]*len(temperatures)

		stack = []

		for currIndex, currTemp in enumerate(temperatures):

			while stack and currTemp > temperatures[stack[-1]]:

				prevIndex = stack.pop()
				result[prevIndex] = currIndex - prevIndex

			stack.append(currIndex)

		while stack:

			result[stack.pop()] = 0

		return result

		