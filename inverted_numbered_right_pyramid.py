


def inverted_numbered_right_pyramid(n):

	"""
	input : number of rows 
	output : 	
			1 2 3 4 5 6
			1 2 3 4 5
			1 2 3 4
			1 2 3
			1 2 
			1
	"""
	num = n

	for i in range(n):
		for j in range(num):
			print(j+1,end=" ")
		num-=1
		print()

if __name__ == "__main__":
	
	n = 6

	inverted_numbered_right_pyramid(n)
    