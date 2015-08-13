#!/usr/bin/python

class Stack:
	def __init__(self, value=None):
		self.data = value
		self.next = None
		if value == None:
			self.length = 0
		else:
			self.length = 1


	# -------------------------------------------
	def isEmpty(self):
		return length == 0


	# -------------------------------------------
	def push(self, value):
		s = Stack(self.data)
		s.next = self.next
		s.length = self.length

		self.next = s
		self.length += 1
		self.data = value


	# -------------------------------------------
	def pop(self):
		if self.length == 0:
			return None

		value = self.data
		self.length -= 1
		
		if self.next != None:
			self.data = self.next.data
			self.next = self.next.next
		else:
			self.data = None

		return value


	# -------------------------------------------
	def peek(self):
		return self.data

	# -------------------------------------------
	def size(self):
		return self.length

	# -------------------------------------------
	def __len__(self):
		return self.length