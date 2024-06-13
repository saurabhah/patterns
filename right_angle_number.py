

def right_angle_number(n):
	"""
	input number of rows 
	output : 	
			1
			1 2
			1 2 3
			1 2 3 4
			1 2 3 4 5
			1 2 3 4 5 6
	"""

	for i in range(n):

		for j in range(i+1):

			print(j+1,end=" ")
		print()


if __name__ == "__main__":
	
	n = 6

	right_angle_number(n)
    