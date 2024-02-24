class Solution:
	
	def addStrings(self,firstStr,secondStr):

		firstIndex, secondIndex = len(firstStr)-1, len(secondStr)-1

		carry, result = 0, []

		while firstIndex >= 0 or secondIndex >= 0 or carry:

			firstDigit = ord(firstStr[firstIndex])-ord('0') if firstIndex >= 0 else 0
			secondDigit = ord(secondStr[secondIndex])-ord('0') if secondIndex >= 0 else 0

			addition = firstDigit+secondDigit+carry

			result.append(chr(addition%10+ord('0')))

			carry = addition // 10

			firstIndex = firstIndex-1 if firstIndex >= 0 else firstIndex
			secondIndex = secondIndex-1 if secondIndex >= 0 else secondIndex

		self.reverse(result)

		return ''.join(result)

	def reverse(self,inputArr):

		left, right = 0, len(inputArr)-1

		while left < right:

			inputArr[left], inputArr[right] = inputArr[right], inputArr[left]
			left += 1
			right -= 1
