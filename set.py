def setornotset(n,num):
    if num & (1 << (n-1)):
              print("set")
    else:
                print("not set")
num=int(input("Enter a number: "))
n=int(input("Enter the bit position: "))
setornotset(n,num)