#write  a program to print all the prime numbers in a given range
a=int(input("enter the number is:"))
b=int(input("enter the number is :"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
        
                