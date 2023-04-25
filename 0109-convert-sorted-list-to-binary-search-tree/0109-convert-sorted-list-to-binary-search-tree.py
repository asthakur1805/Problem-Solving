class Solution:

	def sortedListToBST(self, head):

		nums = []

		curr = head

		while curr:

			nums.append(curr.val)

			curr = curr.next

		print(nums)

		return self.helper(nums, 0, len(nums)-1)

	def helper(self, nums, left, right):

		if left > right:

			return 

		mid = left + (right - left) // 2

		rootNode = TreeNode(nums[mid])
	
		rootNode.left = self.helper(nums, left, mid-1)

		rootNode.right = self.helper(nums, mid+1, right)

		return rootNode