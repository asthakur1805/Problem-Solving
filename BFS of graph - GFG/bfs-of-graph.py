from collections import deque

class Solution:

	def bfsOfGraph(self,numberNodes,adjList):

		numberNodes, visited, result = len(adjList), set({}), []

		self.bfs(adjList,0,visited,result)

		return result

	def bfs(self,adjList,startNode,visited,result):

		queue = deque([startNode])
		visited.add(startNode)

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in adjList[currNode]:

				if neighborNode not in visited:

					queue.append(neighborNode)
					visited.add(neighborNode)

			
	
	

		

		
			
	
	

		

		

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends