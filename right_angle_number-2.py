


def right_angle_number(n):
	"""
	input : number of rows 
	output : 	
		1
		2 2 
		3 3 3
	"""

	for i in range(n):
		num = i
		for j in range(i):
			print(num,end=" ")
		print()	

if __name__ == "__main__":
	
	n = 6

	right_angle_number(n)
    