class Solution:

	def multiply(self, firstNumber, secondNumber):

		if "0" in (firstNumber, secondNumber):
			return "0"

		firstNumberLength, secondNumberLength = len(firstNumber), len(secondNumber)

		builder = [0] * (firstNumberLength + secondNumberLength)

		for secondIndex in range(secondNumberLength-1, -1, -1):

			for firstIndex in range(firstNumberLength-1, -1, -1):

				firstDigit, secondDigit = ord(firstNumber[firstIndex]) - ord("0"), ord(secondNumber[secondIndex]) - ord("0")

				builder[firstIndex + secondIndex + 1] += firstDigit * secondDigit

				builder[firstIndex + secondIndex] += builder[firstIndex + secondIndex + 1] // 10

				builder[firstIndex + secondIndex + 1] %= 10

		zeroPointer = 0

		while builder[zeroPointer] == 0:
			
			zeroPointer += 1

		result = []

		for resultIndex in range(zeroPointer, firstNumberLength + secondNumberLength):

			result.append(chr(builder[resultIndex] + ord('0')))
		
		return ''.join(result)
		