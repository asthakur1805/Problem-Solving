class Solution:

	def nextGreaterElement(self,firstArr,secondArr):

		numsMap = {num : index for index,num in enumerate(firstArr)}

		result = [-1]*len(firstArr)

		for currIndex, val in enumerate(secondArr):

			if val in numsMap:

				updateIndex = numsMap[val]

				for nextIndex in range(currIndex+1,len(secondArr)):

					if secondArr[nextIndex] > val:

						result[updateIndex] = secondArr[nextIndex]
						break

		return result
				

					