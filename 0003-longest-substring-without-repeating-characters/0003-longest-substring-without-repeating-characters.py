class Solution:

	def lengthOfLongestSubstring(self, inputStr):

		startIndex = endIndex = resultLength = 0

		inputLength, charSet = len(inputStr), set()

		while endIndex < inputLength:

			while inputStr[endIndex] in charSet:
				
					charSet.remove(inputStr[startIndex])
					startIndex += 1

			charSet.add(inputStr[endIndex])

			resultLength = max(resultLength, endIndex - startIndex + 1)

			endIndex += 1

		return resultLength
			
			