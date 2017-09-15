import math

print (" program calculate the value of pi")
n= int(input("Enter the number of terms to sum: "))
# name avariable to hold the result (i.e, the sum)
total=0.0
# make another variable to keep track of the sign (+1 or -1)
sign=1.0
for deno in range(1,n,2):
    # add this next term  times the sign into the result
    total= total + sign*4.0/deno
    # flip the sign (multiply by -1)
    sign=-sign
print("Approximation to pi is:", total)
# finally, print the result
print( "different from math.pi:", math.pi-total )

#pi= float((nume/deno)-(nume/(deno+2))+ (nume/(deno+4)))
#print(pi)
                 
                 
    
    
