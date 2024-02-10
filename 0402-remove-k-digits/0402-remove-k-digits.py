class Solution:

	def removeKdigits(self,inputStr,K):

		stack = []

		for digit in inputStr:

			while K > 0 and stack and int(digit) < int(stack[-1]):

				stack.pop()
				K -= 1

			stack.append(digit)

		while K > 0:

			stack.pop()
			K -= 1

		zeroPointer, result = 0, []

		while zeroPointer < len(stack) and stack[zeroPointer] == '0':

			zeroPointer += 1

		for index in range(zeroPointer,len(stack)):

			result.append(stack[index])

		return '0' if not result else ''.join(result)

	

		