import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	correct=0
	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i]:
			correct=correct+1
	return correct/len(y_pred)
	pass