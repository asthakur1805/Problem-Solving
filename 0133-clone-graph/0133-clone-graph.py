class Solution:

	def cloneGraph(self,node):

		if not node:

			return

		oldToNew = {}

		return self.clone(node,oldToNew)

	def clone(self,node,oldToNew):

		if node in oldToNew:

			return oldToNew[node]

		copy = Node(node.val)

		oldToNew[node] = copy

		for neighborNode in node.neighbors:

			copy.neighbors.append(self.clone(neighborNode,oldToNew))

		return copy