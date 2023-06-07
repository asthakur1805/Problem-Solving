class MyStack:

	def __init__(self):

		self.mainQueue = collections.deque([])

		self.tempQueue = collections.deque([])

	def push(self, element):

		self.tempQueue.append(element)

		while self.mainQueue:

			self.tempQueue.append(self.mainQueue.popleft())

		self.tempQueue, self.mainQueue = self.mainQueue, self.tempQueue

	def pop(self):

		return self.mainQueue.popleft()

	def top(self):

		return self.mainQueue[0]

	def empty(self):

		return not self.mainQueue