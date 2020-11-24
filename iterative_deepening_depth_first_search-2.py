class Graph:
	def __init__(self, graph_dict=None, directed=True):
		self.graph_dict = graph_dict or {}
		self.directed = directed
	def get(self, a, b=None):
		links = self.graph_dict.setdefault(a, {})
		if b is None:
			return links
		else:
			return links.get(b)

						#to check the problem and divides into the subproblem
class Problem(object):
	def __init__(self, initial, goal=None):
		self.initial = initial
		self.goal = goal
						#action and value and result are abstract functions so it will be defined later
	def actions(self, state):
		raise NotImplementedError
	def result(self, state, action):
		raise NotImplementedError
	def goal_test(self, state):
		return state == self.goal
	def path_cost(self, c, state1, action, state2):
		return c + 1
	def value(self, state):
		raise NotImplementedError
						#if distance is too too long and not possible to calculate it will give the infinity
infinity = float('inf')
						# initialize the class with superclass
class GraphProblem(Problem):
	def __init__(self, initial, goal, graph):
		Problem.__init__(self, initial, goal)
		self.graph = graph
	def actions(self, A):
		return self.graph.get(A)
						#return destination/goal node
	def result(self, state, action):
		return action
	def path_cost(self, cost_so_far, A, action, B):
		return cost_so_far + (self.graph.get(A, B) or infinity)

						# class Node help in searching of the node
class Node:
	def __init__(self, state, parent=None, action=None, path_cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
						#if parent exist than depth=0
		self.depth = 0
		if parent:
			self.depth = parent.depth + 1
						#used for two string functin
	def __repr__(self):
		return "<Node {}>".format(self.state)
						#it has the same working as BFS and using expand it return the list
	def expand(self, problem):
		return [self.child_node(problem, action)
			for action in problem.actions(self.state)]
							#to find the connected the node if it is exist than it will be stored in next_node
	def child_node(self, problem, action):
		next_state = problem.result(self.state, action)
		new_cost = problem.path_cost(self.path_cost, self.state,action, next_state)        
		next_node = Node(next_state, self, action,new_cost )   
		return next_node
						#trace the path from goal to inital and reversed it.....path functions return the list of object and solutions function returns the state name as list
	def path(self):
		node, path_back = self, []
		while node:
			path_back.append(node)
			node = node.parent
			return list(reversed(path_back))     
	def solution(self):        
		return [node.state for node in self.path()]

							#if current node is goal node it will return it 
def recursive_dls(node, problem, limit):
	if problem.goal_test(node.state):
		return node
							#lf  limit reach to 0 it will return cutoff
	elif limit == 0:
		return 'cutoff'
	else:
							#flag variable is set to be False and it node is found during recursive iteration than it will return it
		cutoff_occurred = False
						#searching recursively to search the node and based on result it return the node , cutoff or not fouund
	for child in node.expand(problem):
		result = recursive_dls(child, problem, limit - 1)
		if result == 'cutoff':
			cutoff_occurred = True
		elif result is not None:
			return result
			return 'cutoff' if cutoff_occurred else 'Not found'
							#it just help to call the recusrive_dls function for first time 
def depth_limited_search(problem, limit=50):
	return recursive_dls(Node(problem.initial), problem, limit)

 							#it calls the depth_limited_searach recusrively with multiple   
def iterative_deepening_search(problem, limit):
	for depth in range(0,limit):
		print("checking with depth :", depth)
		result = depth_limited_search(problem, depth)
		print("result : ", result)

romania_map = Graph(dict( ({
	 'Arad':{'Zerind':75,'Sibiu':140,'Timisoara':118},
	 'Bucharest':{'Urziceni':85,'Pitesti':101,'Giurgiu':90,'Fagaras':211},
     'Craiova':{'Drobeta':120,'Rimnicu':146,'Pitesti':138},
     'Drobeta':{'Mehadia':75,'Craiova':120},
     'Eforie':{'Hirsova':68},
     'Fagaras':{'Sibiu':99,'Bucharest':211},
     'Giurgiu':{'Bucharest':90},
     'Hirsova':{'Urziceni':98,'Eforie':86},
     'Iasi':{'Vaslui':92,'Neamt':87},
     'Lugoj':{'Timisoara':111,'Mehadia':70},
     'Mehadia':{'Lugoj':70,'Drobeta':75},
     'Neamt':{'Iasi':87},
     'Oradea':{'Zerind':71,'Sibiu':151},
     'Pitesti':{'Rimnicu':97,'Craiova':138,'Bucharest':101},
     'Rimnicu':{'Sibiu':80,'Pitesti':97,'Craiova':146},
     'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu':80,'Fagaras':99},
     'Timisoara':{'Arad':118,'Lugoj':111},
     'Urziceni':{'Bucharest':85,'Hirsova':8},
     'Vaslui':{'Iasi':92,'Urziceni':142},
     'Zerind':{'Arad':75,'Oradea':71}
	})),
             False)
#searching the node Neamt from Arad
print("Searching from Arad to Neamt with level 2...")
romania_problem = GraphProblem('Arad','Neamt', romania_map)
print(iterative_deepening_search(romania_problem, 2))
#searching the node Bucharest from Arad
print("Searching from Arad to Bucharest with level 5...")
romania_problem = GraphProblem('Arad','Bucharest', romania_map)
print(iterative_deepening_search(romania_problem, 5))

