import numpy as np

def kernel_function(x1, x2):
	# Your code here
	answer=0
	if len(x1)!=len(x2):
		return 0
	for i in range(len(x1)):
		answer=answer+x1[i]*x2[i]
	return answer
	pass
