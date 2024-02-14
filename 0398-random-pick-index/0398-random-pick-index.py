from random import randint

class Solution:

	def __init__(self,nums):

		self.indices = {}

		for index,num in enumerate(nums):
		
			if num not in self.indices:
	
				self.indices[num] = []

			self.indices[num].append(index)


	def pick(self,target):

		targetIndices = self.indices[target]

		return targetIndices[randint(0,len(targetIndices)-1)]