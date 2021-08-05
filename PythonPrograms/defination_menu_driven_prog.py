def sqr(si=10):#10 is default parameter 
                 area=si*si
                 return area
def cir(r=7):#7 is default parameter
                area=(22/7)*r**2
                return area
def rec(l=5,b=6):
                area =l*b
                return area
ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('1.Find the area of Circle \t')       
                print('2.Find the area of Square \t')
                print('3.Find the area of Rectangle \t')
                choice=input('Enter your choice(1,2,3):')
                if choice=='1':
                                
                                r=int(input('radius of circle: '))
                                print('Area:',cir(r))
                elif choice=='2':
                                
                                si=int(input('side of square:'))
                                print('Area:',sqr(si))
                elif choice=='3':
                                l=int(input('length of reactangle:'))
                                b=int(input('breadth of rectangle:'))
                                print('Area:',rec(l=5,b=6))
                                
                else:
                                print('Invalid Choice')
                ch=input('do you want to continue? (Y,y): ')
