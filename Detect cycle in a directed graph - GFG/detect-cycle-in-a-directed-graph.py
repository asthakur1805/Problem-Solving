class Solution:

	def isCyclic(self,numberNodes,adjList):

		numberNodes = len(adjList)

		visited = [0]*numberNodes

		for startNode in range(numberNodes):

			if visited[startNode] == 0 and self.dfs(adjList,startNode,visited):

				return True

		return False

	def dfs(self,adjList,currNode,visited):

		visited[currNode] = 2

		for neighborNode in adjList[currNode]:

			if (visited[neighborNode] == 0 and self.dfs(adjList,neighborNode,visited)) or visited[neighborNode] == 2:

					return True

		visited[currNode] = 1


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