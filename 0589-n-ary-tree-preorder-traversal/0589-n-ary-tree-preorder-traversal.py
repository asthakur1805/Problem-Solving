class Solution:

	def preorder(self, root):

		if not root:

			return

		result = []

		stack = [(root, False)]

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				for childIndex in range(len(node.children)-1,-1,-1):

					stack.append((node.children[childIndex], False))

				stack.append((node, True))

			else:

				result.append(node.val)

		return result
	