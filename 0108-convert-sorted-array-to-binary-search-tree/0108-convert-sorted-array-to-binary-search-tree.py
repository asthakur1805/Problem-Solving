class Solution:

	def sortedArrayToBST(self, nums):

		return self.helper(nums, 0, len(nums)-1)

	def helper(self, nums, leftPointer, rightPointer):

		if leftPointer > rightPointer:

			return 

		midPointer = leftPointer + (rightPointer - leftPointer) // 2

		rootNode = TreeNode(nums[midPointer])

		rootNode.left = self.helper(nums, leftPointer, midPointer - 1)

		rootNode.right = self.helper(nums, midPointer + 1, rightPointer)

		return rootNode

	