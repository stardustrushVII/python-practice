class Graph:
	def __init__(self, vertices, edges):
		self.vertices = set(vertices)
		self.edges = set(edges)

		# Adjacency list
		self.adjacency_list = {}
		for vertex in vertices:
			self.adjacency_list[vertex] = []

			for edge in edges:
				if vertex in edge:
					for v in edge:
						if v != vertex:
							self.adjacency_list[vertex].append(v)
							break

		# Incidence matrix
		self.incidence_matrix = {}
		for vertex in vertices:
			self.incidence_matrix[vertex] = {}

			for edge in edges:
				if vertex in edge:
					self.incidence_matrix[vertex][edge] = 1
				else:
					self.incidence_matrix[vertex][edge] = 0

		# Adjacency matrix
		self.adjacency_matrix = {}
		for vertex in vertices:
			self.adjacency_matrix[vertex] = {}

			for vertex2 in vertices:
				self.adjacency_matrix[vertex][vertex2] = 0

				for edge in edges:
					if (vertex != vertex2) and (vertex in edge) and (vertex2 in edge):
						self.adjacency_matrix[vertex][vertex2] = 1



g = Graph(
	["a", "b", "c"], 
	[("a", "b"), ("b", "c"), ("a", "c")]
)

print(g.adjacency_list)
print(g.incidence_matrix)
print(g.adjacency_matrix)
