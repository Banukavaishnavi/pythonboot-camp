#print the leap year within a range
a=int(input())
if(a%400==0):
    print("leap yr")
else:
    print("not leap yr")
    a=int(input())
    b=int(input())
    for i in range(a,b+1):
        if(i%4==0 and 1%100!=0):
            print(i)