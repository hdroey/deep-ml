import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	normalized_data=np.zeros(data.shape)
	for i in range(data.shape[1]):
		normalized_data[:,i]=(data[:,i]-data[:,i].min())/(data[:,i].max()-data[:,i].min())


	standardized_data=np.zeros(data.shape)
	for i in range(data.shape[1]):
		standardized_data[:,i]=(data[:,i]-data[:,i].mean())/data[:,i].std()

	return standardized_data, normalized_data