#what makes a star algorithm different is that it has brain and it takes a convincible, sensible  and reasonable action as per functions
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
		print("----->h(n) for ",cities[len(cities)-1],' is ',hn)
		print("------>f(n) for ",citystr,' is ',(hn+gn))
	return (hn+gn)
def expand(mycities,cityq,goal):		
	tot,citystr=mycities
	cities=citystr.split(',')
	city2expand=cities[len(cities)-1]
	if city2expand==goal:
		ans="The a* path is "+citystr+" with the value as "+str(tot)
		while not cityq.empty():
			cityq.get()
		return ans
	print('Expanded city---- ',city2expand)
	for city in dict_gn[city2expand]:
		cityq.put((get_fn(citystr+','+city),citystr+","+city))
def main():	
	start='Arad'
	goal='Bucharest'
	cityq=Q.PriorityQueue()
	cityq.put((get_fn(start) ,start))
	while not cityq.empty():
		mycities=cityq.get()
		ans=expand(mycities,cityq,goal)
		print("Solution ### ",ans)
main()