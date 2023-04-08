class Solution:

	def addBinary(self, firstStr, secondStr):

		firstIndex, secondIndex, result, carry = len(firstStr)-1, len(secondStr)-1, [], 0

		while firstIndex >= 0 or secondIndex >= 0 or carry:

			firstBit = ord(firstStr[firstIndex]) - ord('0') if firstIndex >= 0 else 0
			secondBit = ord(secondStr[secondIndex]) - ord('0') if secondIndex >= 0 else 0

			addition = firstBit + secondBit + carry

			result.append(chr((addition % 2) + ord('0')))

			carry = addition // 2

			firstIndex -= 1

			secondIndex -= 1

		result.reverse()

		return ''.join(result)