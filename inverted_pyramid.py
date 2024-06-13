


def inverted_pyramid(n):
	"""
	input : number of rows 
	output : 	
			* * * * * *
			* * * * * 
			* * * * 
			* * * 
			* * 
			* 
	"""

	for i in range(n,1,-1):
		print(i*"* ")


if __name__ == "__main__":
	
	n = 6

	inverted_pyramid(n)
    