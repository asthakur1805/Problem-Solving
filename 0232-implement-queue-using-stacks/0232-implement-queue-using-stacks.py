class MyQueue:

	def __init__(self):

		self.mainStack = []
		self.tempStack = []

	def push(self, element):

		while self.mainStack:

			self.tempStack.append(self.mainStack.pop())

		self.tempStack.append(element)

		while self.tempStack:

			self.mainStack.append(self.tempStack.pop())

	def pop(self):

		return self.mainStack.pop()

	def peek(self):

		return self.mainStack[-1]

	def empty(self):

		return not self.mainStack