n1=int(input('number1: '))
n2=int(input('number2: '))
n3=int(input('number3: '))
#conditions
if n1>n2:
         if n1>n3:
                 largest=n1
         else:
              largest=n3
else:
     if n2>n3:
             largest=n2
     else:
          largest=n3
#to print largest no
print('largest no: ',largest)
