class Solution:

	def nextGreaterElement(self,firstArr,secondArr):

		numsMap = {num:index for index,num in enumerate(firstArr)}

		result = [-1]*len(firstArr)

		for currIndex,num in enumerate(secondArr):

			if num in numsMap:

				updateIndex = numsMap[num]

				for nextIndex in range(currIndex+1,len(secondArr)):

					if secondArr[nextIndex] > num:

						result[updateIndex] = secondArr[nextIndex]
						break

		return result

		