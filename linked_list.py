class linked_list(object):
	def __init__(self, head=None):
		super(linked_list, self).__init__()
		self.head = head

	def print_list(self):
		current = self.head
		while(current):
			print(current.data)
			current = current.get_next()

	def insert(self, data):
		new_node = node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while(current):
			count+=1
			current = current.get_next()
		return count

	def search(self, searched):
		current = self.head
		while(current):
			if(current.data == searched): return current
			else: current = current.get_next()
		return None

	def delete(self, seaerch, tbd):
		previous = None
		current = self.head
		while(current):
			if(current.data == tbd):
				if(previous is None):
					self.head = current.get_next()
				else:
					previous.set_next(current.get_next())
					return "removed %s" % current
			else:
				previous = current
				current = current.get_next()
		return None


class node(object):
	"""docstring for node"""
	def __init__(self, data=None, next=None):
		super(node, self).__init__()
		self.data = data;
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, next_node):
		self.next = next_node

ll = linked_list()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.print_list()