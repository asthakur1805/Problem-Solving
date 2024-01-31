class Solution:

	def partitionLabels(self,inputStr):

		lastOccur = {}

		for index,currChar in enumerate(inputStr):

			lastOccur[currChar] = index

		result, currPartitionLength, currPartitionEnd = [], 0 , 0

		for index,currChar in enumerate(inputStr):

			currPartitionEnd = max(currPartitionEnd,lastOccur[currChar])

			currPartitionLength += 1

			if index == currPartitionEnd:

				result.append(currPartitionLength)
				currPartitionLength = 0

		return result



			

			