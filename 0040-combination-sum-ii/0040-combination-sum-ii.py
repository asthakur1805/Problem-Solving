class Solution:

	def combinationSum2(self, candidates, target):

		candidates.sort()

		currCombination = []
		result = []
	
		self.helper(candidates, target, 0, currCombination, result)
		
		return result

	def helper(self, candidates, target, index, currCombination, result):

		if target == 0:

			result.append(currCombination.copy())
			return

		if index == len(candidates) or target < 0:

			return

		currCombination.append(candidates[index])
		
		self.helper(candidates, target-candidates[index], index+1, currCombination, result)

		currCombination.pop()

		while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
			
			index += 1	

		self.helper(candidates, target, index+1, currCombination, result)
	