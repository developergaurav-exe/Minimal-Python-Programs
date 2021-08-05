#to count duplicates in a list
n=int(input('TOTAL NO OF ELEMETS:'))
list1=[]
for j in range(0,n):
                e=int(input('ENTER ELEMENT:'))
                list1.append(e)
d=int(input('TO FIND NO OF OCCURENCES:'))
count=0
for i in (list1):
                if (d==i):
                                count=count+1
                                print(d,'has occured',count,'times')
                else:
                                print('NO DUPLICATES FOUND')

