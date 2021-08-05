ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('=====Menu===== \t')
                print('1. Add items to the dictionary \t')
                print('2. Search for an item \t')
                print('3. Display cost of an item \t')
                print('4. Remove an item from the dictionary \t')
                print('5. Display the dictionary \t')
                d1=dict()
                choice=int(input('Enter Your choice(1,2,3,4,5): '))
                if choice==1:
                                n=int(input('How many items do you want to enter?: '))
                                for i in range(0,n):
                                                key=input('Enter the Key: ')
                                                value=int(input('Enter the Value: '))
                                                d1[key]=[value]
                elif choice==2:
                                search=input('Enter the item you want to search: ')
                                for i in range(0,len(d1)):
                                                if i==search:
                                                                print("Item found",search)
                                                                break
                                                else:
                                                                print('Item not found')
                                                                
                elif choice==3:
                                print(d1.values())
                elif choice==4:
                                d=int(input('Enter the item you want to delete: '))
                                del d1[d]
                elif choice==5:
                                print(d1)
                else:
                                print('Invalid Input')
                ch=input('do you want to continue? (Y,y): ')
      
