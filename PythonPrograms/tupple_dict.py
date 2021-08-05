#practice ques.
d1=dict()
choice='y'
while (choice=='y' or choice=='Y'):
                nm=input('enter employee name')
                basic=int(input('enter the basic salary'))
                hra=int(input('enter house rent allowence'))
                con=int(input('enter the conveyance'))
                rec=(basic,hra,con)
                d1[nm]=rec
                choice=input('do you want to continue(y,Y)')
print(d1)
k=d1.keys()
print(k)
print('Name','\t','\t','Total Salary')
for i in k:
                total=0
                rec=d1[i]
                for j in rec:
                                total=total+j
                print(i,'\t','\t',total)
                
