class Solution:

	def postorder(self, root):

		if not root:

			return

		stack = [(root, False)]

		result = []

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				stack.append((node, True))

				for childIndex in range(len(node.children)-1,-1,-1):

					childNode = node.children[childIndex]

					stack.append((childNode, False))

			else:

				result.append(node.val)

		return result