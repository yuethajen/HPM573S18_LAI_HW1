def recursive_summation(n):
    if n==1:
        return 1
    else:
        return n+recursive_summation(n-1)
print(recursive_summation(100))

def iterative_summation(n):
        sum=0
        for i in range(1,n+1):
            sum=sum+i
        return sum
print(iterative_summation(100))

