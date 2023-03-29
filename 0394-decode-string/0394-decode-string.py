class Solution:

	def decodeString(self, inputStr):

		stack, currStr, currNum = [], '', 0

		for char in inputStr:

			if char == '[':

				stack.append(currStr)
				stack.append(currNum)
				currStr, currNum = '', 0

			elif char == ']':

				numRepeats, prevStr = stack.pop(), stack.pop()
				currStr = prevStr + currStr * numRepeats

			elif ord('0') <= ord(char) <= ord('9'):

				currNum = currNum * 10 + ord(char) - ord('0')

			else:

				currStr += char

		return currStr

			
				
			
	