class Solution:

	def myAtoi(self, inputStr):

		index, inputLength = 0, len(inputStr)

		while index < inputLength and inputStr[index] == ' ':
			
			index += 1

		sign, limit = 1, 2**31-1

		if index < inputLength:
			if inputStr[index] == '-':
				sign, limit = -1, limit+1
				index += 1
			elif inputStr[index] == '+':
				index += 1
	
		resultNumber = 0

		while index < inputLength and self.isDigit(inputStr[index]):
			
			digit = ord(inputStr[index])-ord('0')
			
			if resultNumber > (limit - digit) / 10:
				return sign * limit

			resultNumber = resultNumber * 10 + digit

			index += 1

		return sign * resultNumber
			


	def isDigit(self, inputChar):

		return ord('0') <= ord(inputChar) <= ord('9')
			

			
		