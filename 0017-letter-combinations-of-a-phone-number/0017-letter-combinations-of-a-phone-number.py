class Solution:

	def letterCombinations(self, inputStr):

		result = []

		digitsMap = {
			
			'2':'abc',
			'3':'def',
			'4':'ghi',
			'5':'jkl',
			'6':'mno',
			'7':'pqrs',
			'8':'tuv',
			'9':'wxyz'
		}

		currStr = []

		index = 0

		if inputStr:
	
			self.helper(index, inputStr, currStr, result, digitsMap)

		return result

	def helper(self, index, inputStr, currStr, result, digitsMap):

		if index == len(inputStr):

			result.append(''.join(currStr.copy()))
			return

		choices = digitsMap[inputStr[index]]

		for choice in choices:

			currStr.append(choice)
			self.helper(index+1, inputStr, currStr, result,  digitsMap)
			currStr.pop()


		


		

			
