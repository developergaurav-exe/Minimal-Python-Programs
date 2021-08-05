def np():#no. pattern
                for i in range (0,5):
                                for j in range(0,i+1):
                                    print (i,end=" ")
                                print()
                return
def astp():#astrisk pattern
                for i in range (0,3):
                                for j in range(0,i+1):
                                    print ('*',end="")
                                print()
                return
def alp():#alphabet pattern
                for i in range(0,5):
                                chr=65
                                for j in range (1,i+1):
                                                print(chr(asc),end='')
                                                asc+=1
                                print()
                return
def eq_tr_p(n=5):#Equilateral triangle astrisk pattern
                space=n-1
                for i in range(0,n):
                                for j in range(0,space):
                                                print(end='')
                                space=space-1
                                for j in range(0,i+1):
                                                print('*',end='')
                                print('\n')
                return
                
ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('1.To show no. pattern \t')       
                print('2.To show asterisk pattern \t')
                print('3.To show alphabet pattern \t')
                print('4.To show equilateral asterisk pattern \t')
                choice=input('Enter your choice(1,2,3,4):')
                if choice=='1':
                                 np()
                elif choice=='2':
                                 astp()
                elif choice=='3':
                                alp()
                elif choice=='4':
                                eq_tr_p()
                else:
                                print('Invalid Choice.........')
                ch=input('do you want to continue? (Y,y): ')
                
                                
