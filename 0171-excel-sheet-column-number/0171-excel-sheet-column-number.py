class Solution:

	def titleToNumber(self, title):

		result = 0

		for character in title:

			value = ord(character) - ord('A') + 1

			result = result * 26 + value

		return result