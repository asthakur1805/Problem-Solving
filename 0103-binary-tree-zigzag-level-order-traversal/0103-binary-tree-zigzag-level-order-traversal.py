class Solution:

	def zigzagLevelOrder(self, root):

		if not root:
			return

		result = []

		queue = collections.deque([root])

		while queue:

			level = []

			if len(result) % 2:

				for _ in range(len(queue)):

					node = queue.pop()

					level.append(node.val)

					if node.right:

						queue.appendleft(node.right)

					if node.left:

						queue.appendleft(node.left)

			else:

				for _ in range(len(queue)):

					node = queue.popleft()

					level.append(node.val)

					if node.left:

						queue.append(node.left)

					if node.right:

						queue.append(node.right)


			result.append(level)

		return result