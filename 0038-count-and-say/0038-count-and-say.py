class Solution:

	def countAndSay(self, numberTerms):

		result = ['1']

		for _ in range(numberTerms - 1):

			builder, countIndex = [], 0

			while countIndex < len(result):

				character, count = result[countIndex], 0

				while countIndex < len(result) and result[countIndex] == character:

					count += 1
					countIndex += 1
				
				builder.append(str(count))
				builder.append(character)

			result = builder

		return ''.join(result)
