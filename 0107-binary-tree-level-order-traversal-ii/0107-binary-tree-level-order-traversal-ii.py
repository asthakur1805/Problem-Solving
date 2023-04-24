class Solution:

	def levelOrderBottom(self, root):

		if not root:

			return

		stack = []

		result = []

		queue = collections.deque([root])

		while queue:

			level = []

			for _ in range(len(queue)):

				node = queue.popleft()

				level.append(node.val)

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

			stack.append(level)

		while stack:

			result.append(stack.pop())

		return result