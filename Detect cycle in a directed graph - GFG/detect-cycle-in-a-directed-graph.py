class Solution:

	def isCyclic(self, numberNodes, graph):
		
		# Key: Whether node is visited, Value: Whether node is path visited
		visited = {}

		for currNode in range(numberNodes):

			if currNode not in visited:

				if self.dfs(graph, currNode, visited):

					return True

		return False

	def dfs(self, graph, currNode, visited):

		visited[currNode] = True

		for neighborNode in graph[currNode]:

			if neighborNode not in visited:

				if self.dfs(graph, neighborNode, visited):
					return True

			else:

				if visited[neighborNode]:

					return True
		
		visited[currNode] = False
		return False

	

		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends