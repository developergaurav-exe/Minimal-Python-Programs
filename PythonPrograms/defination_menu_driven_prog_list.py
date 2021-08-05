list1=[]
ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('--------------MENU---------------')
                print('1.Add Elements \t')       
                print('2.Modify Elements \t')
                print('3.Delete Elements\t')
                print('4.Sort Elements \t')
                print('5.Display List \t')
                print('6.Exit \t')
                choice=input('Enter your choice(1,2,3,4,5,6):')
                if choice=='1':
                                print('1.ADD ELEMENTS BY APPEND \t')
                                print('2.ADD ELEMENTS BY EXTEND \t')
                                print('3.ADD ELEMENTS BY INSERT \t')
                                add=int(input('ENTER YOUR CHOICE(1,2,3)'))
                                if add==1:
                                                print('-------ADDING ELEMENTS BY APPEND-------')
                                                e=input('ENTER THE ELEMENT:')
                                                list1.append(e)
                                elif add==2:
                                                list2=[10,20,30,40]
                                                print('-------ADDING ELEMENTS BY EXTEND-------')
                                                e=input('ENTER THE ELEMENT:')
                                                list1.extend(list2)
                                elif add==3:
                                                print('-------ADDING ELEMENTS BY INSERT-------')
                                                e=input('ENTER THE ELEMENT:')
                                                po=input('ENTER POSITION(Index)')
                                                list1.insert(e,po)
                elif choice=='2':
                                print('-------MODIFYING-------')
                                n=input('ENTER ITEM TO BE REPLACED:')
                                for i in range(len(list1)):
                                                if(list1[i]==n):
                                                                e=input('ENTER ELEMENT:')
                                                                list1[i]=e
                                                                break
                                                else:
                                                                print(num,'ELEMENT DOES NOT EXIST IN LIST')
                elif choice=='3':
                                print('1.DELETE ELEMENTS THROUGH POSITION')
                                print('2.DELETE ELEMENTS THROUGH VALUE')
                                d=int(input('ENTER YOUR PICK(1,2):'))
                                if d==1:
                                                print('--------DELETING ELEMENTS THROUGH POSITION--------')
                                                index=int(input('ENETR THE POSITION(INDEX):'))
                                                list1.pop(index)
                                elif d==2:
                                                print('--------DELETING ELEMENTS THROUGH VALUE--------')
                                                value=int(input('ENTER THE VALUE(ELEMENT):'))
                                                list1.remove(value)
                elif choice=='4':
                                print('1.SORT IN ASCENDING ORDER')
                                print('2.SORT IN DESCENDING ORDER')
                                s=int(input('ENETR YOUR PICK'))
                                if s==1:
                                                print('------SORTING IN ASCENDING ORDER------')
                                                list1.sort()
                                if s==2:
                                                print('------SORTING IN DESCENDING ORDER------')
                                                list1.sort(reverse=True)
                                                
                                                
                elif choice=='5':
                                print(list1)
                elif choice=='6':
                                break
                else:
                                print('Invalid Choice.........')
                ch=input('Do you want to continue? (Y,n): ')
                print('--------THE END---------')
