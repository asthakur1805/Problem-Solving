class Solution:

	def decodeString(self, inputStr):

		currStr, currNum, stack = '', 0, []

		for char in inputStr:

			if char == '[':

				stack.append(currNum)
				stack.append(currStr)
				currStr, currNum = '', 0

			elif char == ']':

				prevStr, numRepeats = stack.pop(), stack.pop()
				currStr = prevStr + currStr * numRepeats

			elif ord('0') <= ord(char) <= ord('9'):

				currNum = currNum * 10 + ord(char) - ord('0')

			else:

				currStr += char

		return currStr

				
	