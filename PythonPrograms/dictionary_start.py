#1
dict1={'name' : 'Venu','class' : 'XI','rollno.' : 32}
print(dict1)
print(type(dict1))
print(dict1['name'])
for i in dict1:
                print(i," ",dict1[i])
#2
dict2={'XI A':'Science','XI B':'Commerce','XI C':'Humanities'}
for j in dict2:
                print(j,"\t",dict2[j])
#3
n=dict2.keys()
print(n)
m=dict2.values()
print(m)
#4
print('no of key value pairs in the dictionary are ',len(dict1))
for k in dict1:
                print(k,"\t",dict1[k])
#5 to find class from dict2
n2=input('enter the class name which info. to be displayed: ')
for l in dict2:
                if n2==l:
                                print(dict2[l])
                                break
else:
                print('class name invalid')
