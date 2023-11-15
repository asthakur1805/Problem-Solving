from collections import deque

class Solution:

	def topoSort(self,numberNodes,adjList):

		numberNodes, queue, result = len(adjList), deque([]), []

		indegree = {node:0 for node in range(numberNodes)}

		for currNode in range(numberNodes):

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] += 1

		for currNode,degree in indegree.items():

			if degree == 0:

				queue.append(currNode)

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return result


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