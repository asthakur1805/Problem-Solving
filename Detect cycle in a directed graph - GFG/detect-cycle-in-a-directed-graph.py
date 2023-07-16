class Solution:

	def isCyclic(self, numberNodes, graph):

		visited = [0]*len(graph)

		for currNode in range(len(graph)):

			if not visited[currNode] and self.dfs(graph,currNode,visited):

					return True

		return False

	def dfs(self,graph,currNode,visited):

		visited[currNode] = 2

		for neighborNode in graph[currNode]:

			if not visited[neighborNode]: 

				if self.dfs(graph,neighborNode,visited):

					return True

			elif visited[neighborNode] == 2:

				return True

		visited[currNode] = 1
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