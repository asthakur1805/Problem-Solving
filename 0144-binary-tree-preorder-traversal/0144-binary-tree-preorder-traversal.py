class Solution:

	def preorderTraversal(self, root):

		if not root:

			return 


		# Node, toProcess flag
		stack = [(root, False)]

		result = []

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				# Push Right, Left, Root onto the stack

				if node.right:

					stack.append((node.right, False))

				if node.left:

					stack.append((node.left, False))

				stack.append((node, True))


			else:

				result.append(node.val)

		return result
