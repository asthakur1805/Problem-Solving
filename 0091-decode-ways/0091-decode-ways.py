class Solution:

	def numDecodings(self,inputStr):

		return self.helper(inputStr,0,{})

	def helper(self,inputStr,start,cache):

		if start == len(inputStr): return 1

		if inputStr[start] == '0': return 0

		if start in cache: return cache[start]

		singlePartition = self.helper(inputStr,start+1,cache)

		doublePartition = self.helper(inputStr,start+2,cache) if start+1<len(inputStr) and (inputStr[start] == '1' or inputStr[start] == '2' and '0' <= inputStr[start+1] <= '6') else 0

		cache[start] = singlePartition+doublePartition
		return cache[start]

		
		