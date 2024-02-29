class Solution:

	def lengthOfLIS(self,nums):

		return self.helper(nums,0,-1,{})

	def helper(self,nums,currIndex,prevPickedIndex,cache):

		if currIndex == len(nums):

			return 0

		if prevPickedIndex in cache:

			return cache[prevPickedIndex]

		pick = (1 + self.helper(nums,currIndex+1,currIndex,cache)) if prevPickedIndex == -1 or nums[currIndex] > nums[prevPickedIndex] else float('-inf')
		notPick = self.helper(nums,currIndex+1,prevPickedIndex,cache)

		cache[prevPickedIndex] = max(pick,notPick)
		return cache[prevPickedIndex] 