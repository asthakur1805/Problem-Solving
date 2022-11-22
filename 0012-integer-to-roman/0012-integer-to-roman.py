class Solution:

	def intToRoman(self, inputNumber):

		conversion = [
			(1000, 'M'),
			(900, 'CM'),
			(500, 'D'),
			(400, 'CD'),
			(100, 'C'),
			(90, 'XC'),
			(50, 'L'),
			(40, 'XL'),
			(10, 'X'),
			(9, 'IX'),
			(5, 'V'),
			(4, 'IV'),
			(1, 'I')
		]

		romanIndex = 0

		result = []

		while inputNumber:

			baseNumber, roman = conversion[romanIndex]

			if inputNumber >= baseNumber:

				repeat = inputNumber // baseNumber

				result.append(roman * repeat)

				inputNumber %= baseNumber

			romanIndex += 1

		return ''.join(result)

				