class Solution:

	def cloneGraph(self,node):

		if not node:

			return

		oldToNew = {}

		return self.dfs(node,oldToNew)

	def dfs(self,node,oldToNew):

		if node in oldToNew:

			return oldToNew[node]

		copy = Node(node.val)

		oldToNew[node] = copy

		for neighborNode in node.neighbors:

			copy.neighbors.append(self.dfs(neighborNode,oldToNew))

		return copy