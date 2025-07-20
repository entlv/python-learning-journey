import time
def check(num) :
	num=int(input(" enter a number  : "))
	time.sleep(2)
	num %= 2
	if num == 1:
	    print("the number is odd ! ")
	else : 
	    print("the number is even" )


