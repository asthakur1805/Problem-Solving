class Solution:

	def intToRoman(self, inputNumber):

		conversion = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]

		index = 0

		resultRoman = []

		while inputNumber:

			value, symbol = conversion[index]

			if inputNumber >= value:

				repeat = inputNumber // value

				resultRoman.append(symbol*repeat)

				inputNumber %= value

			index += 1

		return ''.join(resultRoman)