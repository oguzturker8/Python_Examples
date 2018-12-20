def Factorial(x):
    if x <1:
        return False
    tmp = 1
    for i in range(1,x+1):
        tmp *= i
    return tmp
while 1:
    print(Factorial((int(input("Number : ")))))
