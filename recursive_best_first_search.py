#iterative bfs uses a queue instead of a stack
#It checks whether a vertex has been discovered before pushing the vertex rather than delaying this check until the vertex is dequeued from the queue

import queue as Q 
dict_hn={'Arad':366,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,'Fagaras':176,'Giurgiu':71,'Hirsova':151,'Iasi':226,'Lugoj':244,'Mehadia':241,'Nemat':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
dict_gn=dict(Arad=dict(Zerind=75,Sibiu=140,Timisoara=118),Bucharest=dict(Urziceni=85,Pitesti=101,Giurgiu=90,Fagaras=211),Craiova=dict(Drobeta=120,Rimnicu=146,Pitesti=138),Drobeta=dict(Mehadia=75,Craiova=120),Eforie=dict(Hirosova=86),Fagaras=dict(Sibiu=99,Bucharest=211),Giurgiu=dict(Bucharest=90),Hirosova=dict(Urziceni=98,Eforie=86),Iasi=dict(Vaslui=92,Neamt=87),Lugoj=dict(Timisoara=111,Mehadia=70),Mehadia=dict(Lugoj=70,Drobeta=75),Neamt=dict(Iasi=87),Oradea=dict(Zerind=71,Sibiu=151),Pitesti=dict(Rimnicu=97,Craiova=138,Bucharest=101),Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),Sibiu=dict(Arad=140,Oradea=151,Rimnicu=80,Fagaras=99),Timisoara=dict(Arad=118,Lugoj=111),Urziceni=dict(Bucharest=85,Hirsova=98),Vaslui=dict(Iasi=92,Urziceni=142),Zerind=dict(Arad=75,Oradea=71) )
def get_fn(citystr):
	cities=citystr.split(',')
	hn=0		#the heuristic estimated cost from node n to the goal node
	gn=0 		#he cost of the path from the start node to n
	ctr=0
	while ctr!=len(cities)-1:
		gn=gn+dict_gn[cities[ctr]][cities[ctr+1]] 	
		ctr=ctr+1
	hn=dict_hn[cities[len(cities)-1]]
	print("----->h(n) for ",cities[len(cities)-1],' is ',hn)
	print("------>f(n) for ",citystr,' is ',(hn+gn))
	return (hn+gn)
def expand(mycities,cityq,goal):		
	tot,citystr=mycities
	cities=citystr.split(',')
	city2expand=cities[len(cities)-1]
	if city2expand==goal:
		ans="The Recursive best path is "+citystr+" with the value as "+str(tot)
		while not cityq.empty():
			cityq.get()
		return ans
	print('Expanded city---- ',city2expand)
	tempq=Q.PriorityQueue()
	for city in dict_gn[city2expand]:
		tempq.put((get_fn(citystr+','+city),citystr+","+city))
		print("First best and second best inserted in priority queue")
		ctr=1
		if(cityq.empty()):
			while not tempq.empty():
				if ctr==1 or ctr==2:
					tempgn,tempstr=tempq.get()
					print("inserting into city queue---> ",tempgn,',',tempstr)
					cityq.put((tempgn,tempstr))
					ctr+=1
				else:
					tempq.get()
		else:
			fn=0
			citystring=''
			fn=getSecondBest(cityq,fn,citystring)
			while not tempq.empty():
				if ctr==1 or ctr==2:
					tempgn,tempstr=tempq.get()
					if tempgn>fn:
						if ctr==1:
							print("inserting into citystr: ",tempgn,",",citystr)
							cityq.put((tempgn,tempstr))
							ctr=3
							continue
						else:
							print("inserting int citystr: ",tempgn,",",citystr)
							ctr=ctr+1
				else:
					tempq.get()
				while not tempq.empty():
					tempq.get()
def getSecondBest(cityq,fn,citystring):
	fn,citystring=cityq.get()
	cityq.put((fn,citystring))	
	return fn
def main():
	start='Arad'
	goal='Bucharest'
	cityq=Q.PriorityQueue()
	cityq.put((get_fn(start),start))
	while not cityq.empty():
		mycities=cityq.get()
		ans=expand(mycities,cityq,goal)
	print('Solution ####',ans)
main()
