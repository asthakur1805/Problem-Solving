class Solution:

	def groupAnagrams(self, inputStrs):

		result = collections.defaultdict(list)

		for str in inputStrs:

			charCounts = [0] * 26

			for character in str:

				charCounts[ord(character)-ord('a')] += 1

			result[tuple(charCounts)].append(str)

		return result.values()