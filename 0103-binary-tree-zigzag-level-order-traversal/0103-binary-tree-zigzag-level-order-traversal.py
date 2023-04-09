class Solution:

	def zigzagLevelOrder(self, root):

		if not root:

			return 

		result = []

		queue = collections.deque([root])

		while queue:

			level = []

			if not len(result) % 2:

				for _ in range(len(queue)):

					node = queue.popleft()

					level.append(node.val)

					if node.left:

						queue.append(node.left)

					if node.right:

						queue.append(node.right)

			else:

				for _ in range(len(queue)):

					node = queue.pop()

					level.append(node.val)

					if node.right:

						queue.appendleft(node.right)

					if node.left:

						queue.appendleft(node.left)

			result.append(level)

		return result