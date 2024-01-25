class Solution:

	def numDecodings(self,inputStr):

		first, second = 1, 0

		for start in range(len(inputStr)-1,-1,-1):

			if inputStr[start] == '0':

				second = first
				first = 0

			else:

				singlePartition = first

				doublePartition = second if start+1<len(inputStr) and (inputStr[start] == '1' or inputStr[start] == '2' and '0' <= inputStr[start+1] <= '6') else 0

				second = first
				first = singlePartition+doublePartition

		return first

