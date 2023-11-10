class Solution:

	def isCycle(self,numberNodes,adjList):

		numberNodes, visited = len(adjList), set({})

		for startNode in range(numberNodes):

			if startNode not in visited and self.dfs(adjList,startNode,None,visited):

				return True

		return False

	def dfs(self,adjList,currNode,parentNode,visited):

		visited.add(currNode)

		for neighborNode in adjList[currNode]:

			if neighborNode not in visited:

				if self.dfs(adjList,neighborNode,currNode,visited):

					return True

			elif neighborNode != parentNode:

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