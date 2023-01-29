class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProducts, postfixProducts, result = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        
        prefix = 1
        
        for index in range(len(nums)):
            
            prefixProducts[index] = prefix
            
            prefix *= nums[index]
            
        postfix = 1
        
        for index in range(len(nums)-1,-1,-1):
        
            postfixProducts[index] = postfix
            
            postfix *= nums[index]
            
        for index in range(len(nums)):
            
            result[index] = prefixProducts[index] * postfixProducts[index]
 
            
        return result