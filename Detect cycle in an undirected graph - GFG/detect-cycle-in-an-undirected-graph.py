from collections import deque

class Solution:

	def isCycle(self, numberNodes, adjList):

		if not numberNodes:

			return False

		visited = set()

		for startNode in range(numberNodes):

			if startNode not in visited and self.bfs(adjList, startNode, visited):

				return True

		return False

	def bfs(self, adjList, startNode, visited):

		visited.add(startNode)
		queue = deque([(startNode, -1)])

		while queue:

			for _ in range(len(queue)):

				currNode, parentNode = queue.popleft()

				for neighborNode in adjList[currNode]:

					if neighborNode not in visited:

						visited.add(neighborNode)
						queue.append((neighborNode, currNode))

					else:

						if neighborNode != parentNode:

							return True

		return False

				
#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends