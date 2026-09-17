
def calculate_brightness(img):
	# Write your code here
	if len(img) == 0:
		 return -1
	counter=0
	for i in range(len(img)):
		if len(img) != len(img[i]):
			return -1
		for j in range(len(img[0])):
			counter=counter+img[i][j]

	counter=counter/(len(img)*len(img[0]))
	return counter
	pass
