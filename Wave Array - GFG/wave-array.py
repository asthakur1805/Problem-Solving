from typing import List


class Solution:

	def convertToWave(self, n, nums):

		for index in range(1, len(nums)):

			if (index % 2 and nums[index] > nums[index-1]) or (not index % 2 and nums[index] < nums[index-1]):

				nums[index], nums[index-1] = nums[index-1], nums[index]



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# } Driver Code Ends