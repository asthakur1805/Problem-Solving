class Solution:

	def countAndSay(self, numberTerms):

		result = ['1']

		for _ in range(numberTerms - 1):

			builder, index = [], 0

			while index < len(result):

				character, count = result[index], 0

				while index < len(result) and result[index] == character:

					count += 1

					index += 1

				builder.append(str(count))
				builder.append(character)

			result = builder

		return ''.join(result)