# Solve prime number by recursion

def prime(n,j):
    if(n<2):
        return False
    if(j==n):
        return True
    if(n%j==0):
        return False
    return prime(n,j+1)

for x in range(100):
    if (prime(x,2)):
        print(x)
