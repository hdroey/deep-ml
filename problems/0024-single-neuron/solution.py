import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities=[]
	for feature in features:
		counter=bias
		for i in range(len(feature)):
			counter=counter+feature[i]*weights[i]
		probabilities.append(1/(1+(math.e**-counter)))
	mse=0
	for i in range(len(probabilities)):
		mse=mse+((probabilities[i]-labels[i])**2)
	mse=mse/len(probabilities)
	return probabilities, mse