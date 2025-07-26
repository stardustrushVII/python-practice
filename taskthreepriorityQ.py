class PriorityQueue:
	def __init__(self, data):
		# store initial data by prio 
		self.queue = sorted(data, key=lambda x: x[1])

	def get(self):
		if not self.queue:
			return None
		return self.queue.pop(0)[0] # return name, not prio


	def add(self, data):
		self.queue.append(data)
		self.queue.sort(key=lambda x: x[1]) # sort again by prio

	def peek(self):
		if not self.queue:
			return None
		return self.queue[0][0] # return item with higest prio





# queue_data = [
# 	("Robert", 1),
# 	("Jane", 4),
# 	("Alex", 2),
# 	("Robert", 1)
# ]
# queue = PriorityQueue(queue_data)

# print(queue.get())
# queue.add(("", 2))
# print(queue.get())