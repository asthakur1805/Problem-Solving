class MyQueue:

	def __init__(self):

		self.pushStack = []
		self.popStack = []

	def push(self,element):

		self.pushStack.append(element)

	def pop(self):

		if not self.popStack:

			while self.pushStack:

				self.popStack.append(self.pushStack.pop())

		return self.popStack.pop()

	def peek(self):

		if not self.popStack:

			while self.pushStack:

				self.popStack.append(self.pushStack.pop())

		return self.popStack[-1]

	def empty(self):

		return not self.pushStack and not self.popStack