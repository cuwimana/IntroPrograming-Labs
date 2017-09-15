    # Fibibacci.py
    # nth fibacci number

def main():
    print(" this program calculate nth Fibonacci value")
    print()

    n=int(input("Enter the value of n: "))
    X= 1
    Y= 1
    for i in range(n-2):
        X,Y= X+Y,X
    print()
    print("the nth Fibonacci number is",X)
    
          
    
