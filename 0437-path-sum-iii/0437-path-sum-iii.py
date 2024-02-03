class Solution:

	def pathSum(self,root,targetSum):

		self.result = 0

		currPathSum, cache = 0, {0:1}

		self.preorder(root,targetSum,currPathSum,cache)

		return self.result

	def preorder(self,node,targetSum,currPathSum,cache):

		if not node:

			return 

		currPathSum += node.val

		prefixSum = currPathSum - targetSum

		self.result += cache.get(prefixSum,0)

		cache[currPathSum] = cache.get(currPathSum,0) + 1

		self.preorder(node.left,targetSum,currPathSum,cache)
		self.preorder(node.right,targetSum,currPathSum,cache)

		cache[currPathSum] -= 1

		