class Solution:

	def inorderTraversal(self, root):

		if not root:

			return

		result = []

		# Node, ToProcess Flag
		stack = [(root, False)]

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				# Push Right, Root, Left onto stack

				if node.right:
					
					stack.append((node.right, False))

				stack.append((node, True))

				if node.left:

					stack.append((node.left, False))

			else:

				result.append(node.val)


		return result