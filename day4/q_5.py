string=input()
n="@/"
count=0
for i in string:
    if (i in n[0] or n[1] and i!=" "):
        count+=1
        break
    else:
        print("follow the condition")
if(len(string)<8):
    print("follow the conditions")
elif(len(string) >8 and len(string)<12):
    print("password is strong")
elif(len(string)<12 and len(string)<15):
    print("password is strong")
else:
    print("password is weak")