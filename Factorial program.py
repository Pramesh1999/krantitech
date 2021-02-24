#Python3 program To calculate
# The Value Of nCr
#create method and passing arguments using recur
def nCr(n, r):
    return (fact(n) / (fact(r)
                       * fact(n - r)))
# Returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res
# Driver code
#Taking input from users
n = int(input("enter total integer"))
r = int(input("enter selection integer"))
#print Value  of nCr
print(int(nCr(n, r)))


# out Put
# enter total integer10
# enter selection integer1
# 10
