class Solution:

	def deleteAndEarn(self,nums):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1

		nums = sorted(set(nums))

		return self.helper(nums,len(nums)-1,False,counts,{})

	def helper(self,nums,index,isNextDeleted,counts,cache):

		if index < 0:

			return 0

		if (index,isNextDeleted) in cache:

			return cache[(index,isNextDeleted)]

		deleteCurr = 0 

		if not isNextDeleted or nums[index] != nums[index+1]-1:

			deleteCurr = counts[nums[index]] * nums[index] + self.helper(nums,index-1,True,counts,cache)

		notDeleteCurr = self.helper(nums,index-1,False,counts,cache)

		cache[(index,isNextDeleted)] = max(deleteCurr,notDeleteCurr)
		return cache[(index,isNextDeleted)]