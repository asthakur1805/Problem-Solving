class Solution:

	def topoSort(self,numberNodes,adjList):

		numberNodes, stack, result, visited = len(adjList), [], [], set({})

		for startNode in range(numberNodes):

			if startNode not in visited:

				self.dfs(adjList,startNode,visited,stack)
		
		while stack:

			result.append(stack.pop())

		return result

	def dfs(self,adjList,currNode,visited,stack):

		visited.add(currNode)

		for neighborNode in adjList[currNode]:

			if neighborNode not in visited:

				self.dfs(adjList,neighborNode,visited,stack)

		stack.append(currNode)


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends