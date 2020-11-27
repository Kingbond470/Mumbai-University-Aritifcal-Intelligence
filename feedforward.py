# feed forward-- the infromation travels only in forward way-----> through input nodes than through hiddeen layers and finally through the output nodes
import math
# calculating the neuron activation for an input
def activate (weights,inputs):
	activation=weights[-1]		#weights-->network weight
	for i in range (len(weights)-1):		# i is the index of a weights
		activation+=weights[i]*inputs[i]
	return activation
def transfer(activation):		# neuron is activated and for transfer the activation this function is used.
	return 1.0/(1.0+math.e**(-activation))		#sigmoid/logistic function--it takes any input and produce the number betweeen 0 and 1
def forward_propogation(network,row):		# here, the input is straight forward---calculating the output for each neurons and output from one layer becomes the inputs to the neurons on next layer
	inputs=row
	for layer in network:	
		new_input=[]
		for neurons in layer:
			activation=activate(neurons['weights'],inputs)
			neurons['output']=transfer(activation)
			print("The neurons are: "+str(neurons))		
			new_input.append(neurons['output'])
		inputs=new_input
		print(inputs)
	return inputs
# initialize a network
network=[[{'weights':[0.12436424411240122,0.847433,0.587687587]}],[{'weights':[0.45345234235435,0.2542352342345]}],[{'weights':[0.453452349765,0.254982345]}]]
row=[1,0,None]
output=forward_propogation(network,row)
print("The output is:"+str(output))