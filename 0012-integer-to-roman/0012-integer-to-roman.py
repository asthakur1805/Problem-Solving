class Solution:

	def intToRoman(self, inputNumber):

		result, romanIndex = [], 0

		mapping = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

		while inputNumber:

			base, roman = mapping[romanIndex]

			numRepeats = inputNumber // base

			if numRepeats > 0:

				result.append(roman * numRepeats)

				inputNumber %= base

			romanIndex += 1

		return ''.join(result)

			