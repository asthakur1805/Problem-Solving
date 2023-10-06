from collections import deque

class MyStack:

	def __init__(self):

		self.mainQueue = deque([])
		self.tempQueue = deque([])

	def push(self,element):

		self.tempQueue.append(element)

		while self.mainQueue:

			self.tempQueue.append(self.mainQueue.popleft())

		self.mainQueue, self.tempQueue = self.tempQueue, self.mainQueue

	def pop(self):

		return self.mainQueue.popleft()

	def top(self):

		return self.mainQueue[0]

	def empty(self):

		return not self.mainQueue
		