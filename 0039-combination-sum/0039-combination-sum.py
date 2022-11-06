class Solution:

	def combinationSum(self, candidates, target):

		result = []

		self.helper(candidates, target, result)

		return result

	def helper(self, candidates, target, result, index=0, currCombination=[]):

		if index == len(candidates) or target < 0:

			return

		if target == 0:

			result.append(currCombination.copy())
			return

		currCombination.append(candidates[index])
		
		self.helper(candidates, target-candidates[index], result, index, currCombination)

		currCombination.pop()

		self.helper(candidates, target, result, index+1, currCombination)


		
		
		

