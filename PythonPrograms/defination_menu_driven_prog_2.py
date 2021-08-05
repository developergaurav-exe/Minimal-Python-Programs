def fac(n=2):
                f=1
                for i in range(n):
                                f=f*(i+1)
                return f
def arm(n=407):
                sum=0
                arm=n
                while arm>0:
                                nu=arm%10
                                sum+=nu**3
                                arm//=10
                if n==sum:
                                print('It is an Armstrong Number i.e.',n)
                else:
                                print('Its is not an Armstong Number i.e.:',n)
                return arm
                
ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('1.Find Factorial \t')       
                print('2.Find Armstrong Number \t')
                choice=input('Enter your choice(1,2):')
                if choice=='1':
                                n=eval(input('enter no: '))
                                print('Factorial:',fac(n))
                elif choice=='2':
                                n=eval(input('enter no: '))
                                print(arm(n))
                                
                else:
                                print('Invalid Choice')
                ch=input('do you want to continue? (Y,y): ')
