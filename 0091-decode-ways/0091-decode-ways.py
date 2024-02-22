class Solution:

	def numDecodings(self,inputStr):

		singlePartitionResult, doublePartitionResult = 1, 0

		for start in range(len(inputStr)-1,-1,-1):

			if inputStr[start] == '0':

				doublePartitionResult, singlePartitionResult = singlePartitionResult, 0

			else:

				singlePartition = singlePartitionResult

				if start+1<len(inputStr) and (inputStr[start] == '1' or (inputStr[start] == '2' and 0 <= int(inputStr[start+1]) <= 6)):

					doublePartition = doublePartitionResult

				else:
	
					doublePartition = 0

				doublePartitionResult, singlePartitionResult = singlePartitionResult, singlePartition + doublePartition

		return singlePartitionResult
		
		