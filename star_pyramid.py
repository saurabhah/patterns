


def inverted_numbered_right_pyramid(n):

	"""
	input : number of rows 
	output : 	
		     *     
		    ***    
		   *****   
		  *******  
		 ********* 
		***********
	"""
	k = 0

	for i in range(1, n+1):
	    for space in range(1, (n-i)+1):
	        print(end="  ")
	   
	    while k!=(2*i-1):
	        print("* ", end="")
	        k += 1
	   
	    k = 0
	    print()

		
if __name__ == "__main__":
	
	n = 6

	inverted_numbered_right_pyramid(n)
    