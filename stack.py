class Stack():
	def __init__(self):
		self.stack_list = []
	
	def push(self,data):
		self.stack_list.insert(0,data)
		return self.stack_list
		
	def pop(self,data):
		if len(self.stack_list) > 0:
			l_index = self.stack_list.index(data)
			return self.stack_list.pop(l_index)
		else:
			print "The list is null"
			return self.stack_list
		
	def clear(self):
		if len(self.stack_list)>0:
			self.stack_list = []
			return self.stack_list
			
list = Stack()
a = list.push(2)
a = list.push(3)
a = list.push(4)
print "push 2,3,4", a
b = list.pop(2)
print "after pop 2",b,a
a = list.clear()
print "after clear",a

