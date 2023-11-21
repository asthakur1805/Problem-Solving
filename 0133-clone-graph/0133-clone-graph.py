from collections import deque

class Solution:

	def cloneGraph(self,node):

		if not node:

			return 

		copy = Node(node.val)

		oldToNew = {node:copy}

		queue = deque([node])

		while queue:

			oldNode = queue.popleft()

			for neighborNode in oldNode.neighbors:

				if neighborNode not in oldToNew:

					neighborCopy = Node(neighborNode.val)

					oldToNew[neighborNode] = neighborCopy

					queue.append(neighborNode)

				oldToNew[oldNode].neighbors.append(oldToNew[neighborNode])

		return copy

		
				