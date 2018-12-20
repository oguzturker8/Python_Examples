def Armstrong(x):
    tmp = 0
    for i in range(1, len(str(x))+1):
        y = int((x % pow(10,i) / pow(10, i-1))) 
        tmp += pow(y,3)
    if x == tmp:
        return True
    else:
        return False
while 1:
    print(Armstrong((int(input("Number : ")))))
