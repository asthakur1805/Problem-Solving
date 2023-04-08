class Solution:

	def romanToInt(self, inputStr):

		mapping = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000
		}

		index, result = 0, 0

		while index < len(inputStr)-1:

			if mapping[inputStr[index]] < mapping[inputStr[index+1]]:

				result += mapping[inputStr[index+1]] - mapping[inputStr[index]]

				index += 2

			else:

				result += mapping[inputStr[index]]

				index += 1

		if index < len(inputStr):

			result += mapping[inputStr[-1]]

		return result