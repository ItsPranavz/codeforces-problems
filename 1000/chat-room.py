s=str(input())
 
counter=0
for i in s:
    if counter==0 and i=='h':
        counter=counter+1
    elif counter==1 and i=='e':
        counter=counter+1
    elif counter==2 and i=='l':
        counter=counter+1
    elif counter==3 and i=='l':
        counter=counter+1
    elif counter==4 and i=='o':
        counter=counter+1
if(counter==5):
    print("YES")
else:
    print("NO")
