class Solution:

	def characterReplacement(self,inputStr,maxReplacements):

		start, counts, result, maxCount = 0, [0]*26, 0, 0

		for end in range(len(inputStr)):

			counts[ord(inputStr[end])-ord('A')] += 1
			maxCount = max(maxCount,counts[ord(inputStr[end])-ord('A')])

			while (end-start+1) - maxCount > maxReplacements:

				counts[ord(inputStr[start])-ord('A')] -= 1
				start += 1

			result = max(result,end-start+1)

		return result