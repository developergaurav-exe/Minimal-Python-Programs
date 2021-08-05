ch=input('do you want to start the program (Y,y): ')
while ch=="y" or ch=='Y':
                print('=====Menu=====')
                print('1. Display the no of days in a month \t')
                print('2. Display Months in alphabetical order \t')
                print('3. Display months with 31 days \t')
                print('4. Display months sorted by no of days \t')
                d1={'jan':31,'feb':29,'mar':31,'apr':30,'may':31,'june':30,'july':31,'aug':30,'sep':31,'oct':30,'dec':31}
                choice=int(input('Enter your choice(1,2,3,4): '))
                if choice==1:
                                search=input('Enter the month: ')
                                s=d1.get(search)
                                print(s)
                elif choice==2:
                                k=d1.keys()
                                print('Months in alpahabetical order \t',sorted(k))
                elif choice==3:
                                k=d1.keys()
                                for i in k:
                                                a=d1[i]
                                                if a==31:
                                                                print(i)
                elif choice==4:
                                v=d1.keys()
                                print('Months sorted by no of days \t',sorted(v,reverse=True))
                else:
                                print('Invalid Input')
                ch=input('do you want to continue? (Y,y): ')
