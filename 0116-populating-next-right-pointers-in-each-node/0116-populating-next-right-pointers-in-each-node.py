class Solution:

	def connect(self, root):

		if not root:
			return

		queue = collections.deque([root])

		while queue:

			levelCount = len(queue)

			for nodeNumber in range(levelCount):

				node = queue.popleft()

				if node:
					
					node.next = None if nodeNumber == levelCount-1 else queue[0]
				
					queue.append(node.left)

					queue.append(node.right)

		return root
		