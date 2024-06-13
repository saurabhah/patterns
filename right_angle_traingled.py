

def right_angle_traingle(n):
	"""
	input number of rows 
	output : 	
			* 
			* * 
			* * *
			* * * *
			* * * * *
	"""

	for i in range(n+1):

		print(i*"* ")


if __name__ == "__main__":
	
	n = 5

	right_angle_traingle(n)
    