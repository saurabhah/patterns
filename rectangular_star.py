

def rectangular_star(n):
	"""
	input number of rows 
	output : 	
				*****
				*****
				*****
				*****
				*****
	"""

	for i in range(n):

		print(n*"*")


if __name__ == "__main__":
	
	n = 5

	rectangular_star(n)
    