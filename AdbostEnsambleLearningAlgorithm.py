# Adbost Ensamble Learning Algorithm -->>> combining the predictions from many learners........it is done by weighing the training dataset to put  more focus on training examples on which prior models  made prediction errors
class Perceptron:	
	def __init__(self,a,b,c,tval):		# initialize variable
		self.x=a
		self.result=b
		self.cresult=c
		self.threshold=tval
		self.w=[]
	def h(self,tw):
		hresult=[]
		for i in range(0,len(self.result)):
			hresult.append(0)
										#print("index-->",i,";",hresult)
			for j in range(0,len(tw)):
				hresult[i]=hresult[i]+(tw[j][i]*self.x[j][i])
		return hresult
	def checkthreshold(self,hresult):
										#flag=True
		actfun=[]
		for i in range(0,len(self.result)) :	
			if(hresult[i]<=self.threshold):
				actfun.append(0)
			else:
				actfun.append(1)
		print("Ans:",hresult)
		print("Result of act function: ",actfun)
		for i in range(0,len(self.x)):
			if (actfun[i]!=self.result[i]):
				return False
		return True
	def training(self,tw,a):
										#passing w vector and alpha
		i=1
		while i<=100:
			print("Attemp: ",i)
			hresult=self.h(tw)
			if (self.checkthreshold(hresult)):
										#if training result mathches the test result
				self.w=tw
				print("In attempt number ",i," I got it !! I think I have.. ")
				for x in range(0,len(self.w)):
					print("w",x,"--> ",self.w [x])
				break
			i=i+1
			for j in range(0,len(self.result)):
				for k in range(0,len(tw)):
					sum=0
					for n in range(0,len(tw)):
						sum=sum+(self.cresult[j]-hresult[j])*self.x[n][j]
						tw[k][j]=tw[k][j]+a*sum
		if (i>=100):
			print("I'm prettyexhausted, tried 100 iteration so...change it !! ")
a=[[1,1,1,1],[0,0,1,1],[0,1,0,1]]
b=[0,1,1,1]
c=[0.5,0.7,1.3,1.5]
p=Perceptron(a,b,c,0.5)
print("Whether Reservation is done: ",p.x[0])
print("Whethe Raining outside: ",p.x[1])
print("With Threshold value: ",p.threshold)
r=p.h( [ [ 0.5,0.5,0.5,0.5 ], [ 0.8,0.8,0.8,0.8 ], [ 0.2,0.2,0.2,0.2 ] ] )
print("Status: ",p.checkthreshold(r))

print("Example 1 --> 0.01")
p.training([ [0.7,0.7,0.7,0.7],[0.5,0.5,0.5,0.5],[0.4,0.4,0.4,0.4] ],0.01)	

print("Example 2 --> 0.5")
p.training([ [0.7,0.7,0.7,0.7],[0.5,0.5,0.5,0.5],[0.4,0.4,0.4,0.4] ],0.5)		

print("Example 3 --> 0.01")
p.training([ [0.2,0.2,0.2,0.2],[0.3,0.3,0.3,0.3],[0.5,0.5,0.5,0.5] ],0.01)				