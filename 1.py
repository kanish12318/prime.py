def numofbits(n):
    ones=0
    zeroes=0
    while (n):
        if (n & 1):
            ones+=1
        else:
            zeroes+=1
        n>>=1

    print("number of ones:", ones, "number of zeroes:", zeroes)
num=int(input("Enter a number: "))
numofbits(num)