age={10:0,20:0,30:0,40:0,50:0,60:0,70:0,80:0,90:0,100:0}
l=[10,20,30,40,45,50,60]
for i in l:
    if i>=1 and i<=10:
        age[10]+=1
    if i>=11 and i<=20:
        age[20]+=1
    if i>=21 and i<=30:
        age[30]+=1
    if i>=31 and i<=40:
        age[40]+=1
    if i>=41 and i<=50:
        age[50]+=1
    if i>=51 and i<=60:
        age[60]+=1
    if i>=61 and i<=70:
        age[70]+=1
    if i>=71 and i<=80:
        age[80]+=1
    if i>=81 and i<=90:
        age[90]+=1
    if i>=91 and i<=100:
        age[100]+=1
print("Agegroup","Total number of people") 
for i,j in age.items():
    print((i-9),'-',i,"  ",j)
