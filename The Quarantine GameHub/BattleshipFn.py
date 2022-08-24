def battleship():
    import sys
    import time

    l = [[' ','A','B','C','D','E','F','G','H','I'],
         ['1','O','O','O','O','O','O','O','O','O'],
         ['2','O','O','O','O','O','O','O','O','O'],
         ['3','O','O','O','O','O','O','O','O','O'],
         ['4','O','O','O','O','O','O','O','O','O'],
         ['5','O','O','O','O','O','O','O','O','O'],
         ['6','O','O','O','O','O','O','O','O','O'],
         ['7','O','O','O','O','O','O','O','O','O'],
         ['8','O','O','O','O','O','O','O','O','O'],
         ['9','O','O','O','O','O','O','O','O','O']]

    lopp = [[' ','A','B','C','D','E','F','G','H','I'],
         ['1','O','O','O','O','O','O','O','O','O'],
         ['2','O','O','O','O','O','O','O','O','O'],
         ['3','O','O','O','O','O','O','O','O','O'],
         ['4','O','O','O','O','O','O','O','O','O'],
         ['5','O','O','O','O','O','O','O','O','O'],
         ['6','O','O','O','O','O','O','O','O','O'],
         ['7','O','O','O','O','O','O','O','O','O'],
         ['8','O','O','O','O','O','O','O','O','O'],
         ['9','O','O','O','O','O','O','O','O','O']]

    marker = [[' ','A','B','C','D','E','F','G','H','I'],
         ['1','O','O','O','O','O','O','O','O','O'],
         ['2','O','O','O','O','O','O','O','O','O'],
         ['3','O','O','O','O','O','O','O','O','O'],
         ['4','O','O','O','O','O','O','O','O','O'],
         ['5','O','O','O','O','O','O','O','O','O'],
         ['6','O','O','O','O','O','O','O','O','O'],
         ['7','O','O','O','O','O','O','O','O','O'],
         ['8','O','O','O','O','O','O','O','O','O'],
         ['9','O','O','O','O','O','O','O','O','O']]

    alphanum = [' ','A','B','C','D','E','F','G','H','I']

    #----------------------------------WELCOME-PAGE-------------------------------------------------------#

    print("\n\n**Welcome To BATTLESHIPS**\n\n")
    time.sleep(3)
    print("\n\nYour Board\n\n")
    for x in l:
        print(*x)
    time.sleep(3)
    print("\n\nLet's Place your Ships\n\n")
    time.sleep(2)

    #----------------------------------USER-INPUT-------------------------------------------------------#

    while 1<2:
        try:
            print("\nPlace Aircraft Carrier (5): \n")
            a = input("\nEnter first position (A1,B3,etc.): ")
            b1 = a[0].upper()
            c1 = int(a[1])

            b1 = alphanum.index(b1)
            a = input("\nEnter final position (A1,B3,etc.): ")
            b2 = a[0].upper()
            c2 = int(a[1])

            b2 = alphanum.index(b2)

            if b1==b2 and abs(int(c1)-(int(c2)+1))==5 or b1==b2 and abs((int(c1)+1)-(int(c2)))==5:
                minc = min(int(c1),int(c2))
                maxc = max(int(c1),int(c2))
                
                for x in range(minc,maxc+1):
                    l[x][b1] = 'A'
                break

            elif c1==c2 and abs(b1-b2)==4:
                minb = min(int(b1),int(b2))
                maxb = max(int(b1),int(b2))
                
                for x in range(minb,maxb+1):
                    l[c1][x] = 'A'
                break

            else:
                print("\nCannot Place that way, Try Again\n")
        except:
            print("\nEntry not allowed\n")

    print('\n')
    for x in l:
        print(*x)

    while 1<2:
        try:
            print("\nPlace Battleship (4): ")
            a = input("\nEnter first position (A1,B3,etc.): ")
            b1 = a[0].upper()
            c1 = int(a[1])

            b1 = alphanum.index(b1)
            a = input("\nEnter final position (A1,B3,etc.): ")
            b2 = a[0].upper()
            c2 = int(a[1])

            b2 = alphanum.index(b2)

            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            for x in range(minc,maxc+1):
                    if l[x][b1] != 'O':
                        print("\nShip colliding with another ship ")
                        b1 = -10
                        c1 = -10
                        break

            if b1==b2 and abs(int(c1)-(int(c2)+1))==4 or b1==b2 and abs((int(c1)+1)-(int(c2)))==4:
                minc = min(int(c1),int(c2))
                maxc = max(int(c1),int(c2))

                
                
                for x in range(minc,maxc+1):
                    l[x][b1] = 'B'
                break

            elif c1==c2 and abs(b1-b2)==3:
                minb = min(int(b1),int(b2))
                maxb = max(int(b1),int(b2))
                
                for x in range(minb,maxb+1):
                    l[c1][x] = 'B'
                break

            else:
                print("\nCannot Place that way, Try Again\n")
        except:
            print("\nEntry not allowed\n")

    print('\n')

    for x in l:
        print(*x)

    while 1<2:
        try:
            print("\nPlace Cruiser (3): \n")
            a = input("\nEnter first position (A1,B3,etc.): ")
            b1 = a[0].upper()
            c1 = int(a[1])

            b1 = alphanum.index(b1)
            a = input("\nEnter final position (A1,B3,etc.): ")
            b2 = a[0].upper()
            c2 = int(a[1])

            b2 = alphanum.index(b2)

            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            for x in range(minc,maxc+1):
                    if l[x][b1] != 'O':
                        print("\nShip colliding with another ship \n")
                        b1 = -10
                        c1 = -10
                        break

            if b1==b2 and abs(int(c1)-(int(c2)+1))==3 or b1==b2 and abs((int(c1)+1)-(int(c2)))==3:
                minc = min(int(c1),int(c2))
                maxc = max(int(c1),int(c2))

                
                
                for x in range(minc,maxc+1):
                    l[x][b1] = 'C'
                break

            elif c1==c2 and abs(b1-b2)==2:
                minb = min(int(b1),int(b2))
                maxb = max(int(b1),int(b2))
                
                for x in range(minb,maxb+1):
                    l[c1][x] = 'C'
                break

            else:
                print("\nCannot Place that way, Try Again\n")
        except:
            print("\nEntry not allowed\n")

    print('\n')
    for x in l:
        print(*x)

    while 1<2:
        try:
            print("\nPlace Submarine (3): \n")
            a = input("Enter first position (A1,B3,etc.): ")
            b1 = a[0].upper()
            c1 = int(a[1])

            b1 = alphanum.index(b1)
            a = input("\nEnter final position (A1,B3,etc.): ")
            b2 = a[0].upper()
            c2 = int(a[1])

            b2 = alphanum.index(b2)

            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            for x in range(minc,maxc+1):
                    if l[x][b1] != 'O':
                        print("\nShip colliding with another ship \n")
                        b1 = -10
                        c1 = -10
                        break

            if b1==b2 and abs(int(c1)-(int(c2)+1))==3 or b1==b2 and abs((int(c1)+1)-(int(c2)))==3:
                minc = min(int(c1),int(c2))
                maxc = max(int(c1),int(c2))

                
                
                for x in range(minc,maxc+1):
                    l[x][b1] = 'S'
                break

            elif c1==c2 and abs(b1-b2)==2:
                minb = min(int(b1),int(b2))
                maxb = max(int(b1),int(b2))
                
                for x in range(minb,maxb+1):
                    l[c1][x] = 'S'
                break

            else:
                print("\nCannot Place that way, Try Again\n")
        except:
            print("\nEntry not allowed\n")

    print('\n')
    for x in l:
        print(*x)





    while 1<2:
        try:
            print("\nPlace Destroyer (2): \n")
            a = input("\nEnter first position (A1,B3,etc.): ")
            b1 = a[0].upper()
            c1 = int(a[1])

            b1 = alphanum.index(b1)
            a = input("\nEnter final position (A1,B3,etc.): ")
            b2 = a[0].upper()
            c2 = int(a[1])

            b2 = alphanum.index(b2)

            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            for x in range(minc,maxc+1):
                    if l[x][b1] != 'O':
                        print("\nShip colliding with another ship \n")
                        b1 = -10
                        c1 = -10
                        break

            if b1==b2 and abs(int(c1)-(int(c2)+1))==2 or b1==b2 and abs((int(c1)+1)-(int(c2)))==2:
                minc = min(int(c1),int(c2))
                maxc = max(int(c1),int(c2))

                
                
                for x in range(minc,maxc+1):
                    l[x][b1] = 'D'
                break

            elif c1==c2 and abs(b1-b2)==1:
                minb = min(int(b1),int(b2))
                maxb = max(int(b1),int(b2))
                
                for x in range(minb,maxb+1):
                    l[c1][x] = 'D'
                break

            else:
                print("\nCannot Place that way, Try Again\n")
        except:
            print("\nEntry not allowed\n")

    print('\n')
    for x in l:
        print(*x)


    #----------------------------------COMPUTER-INPUT-------------------------------------------------------#

    import random

    print("\nComputer: \n")

    time.sleep(2)

    print("\nComputer Placing Aircraft Carrier: \n")
    while 1<2:
        
        compfirst = (random.choice(['A','B','C','D','E'])+str(random.randint(1,4)))
        b1 = compfirst[0]
        c1 = int(compfirst[1])

        b1 = alphanum.index(b1)

        compfinal = (random.choice([f'{alphanum[b1+4] + str(c1)}',f'{alphanum[b1]+str(c1+4)}']))
        b2 = compfinal[0]
        c2 = int(compfinal[1])

        b2 = alphanum.index(b2)
        minc = min(int(c1),int(c2))
        maxc = max(int(c1),int(c2))
        
        minb = min(int(b1),int(b2))
        maxb = max(int(b1),int(b2))
        
        if b1==b2:
            for x in range(minc,maxc+1):
                    if lopp[x][b1] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break
        if c1==c2:
            for x in range(minb,maxb+1):
                    if lopp[c1][x] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break

        if b1==b2 and abs(int(c1)-(int(c2)+1))==5 or b1==b2 and abs((int(c1)+1)-(int(c2)))==5: #or c1==c2 and abs(b1-b2)==5:
            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))
            
            for x in range(minc,maxc+1):
                lopp[x][b1] = 'A'
            break

        elif c1==c2 and abs(b1-b2)==4:
            minb = min(int(b1),int(b2))
            maxb = max(int(b1),int(b2))
            
            for x in range(minb,maxb+1):
                lopp[c1][x] = 'A'
            break

        else:
           pass

    time.sleep(2)

    print("\nComputer Placing Battleship: \n")

    while 1<2:
       
        compfirst = (random.choice(['A','B','C','D','E'])+str(random.randint(1,5)))
        b1 = compfirst[0]
        c1 = int(compfirst[1])

        b1 = alphanum.index(b1)

        compfinal = (random.choice([f'{alphanum[b1+3] + str(c1)}',f'{alphanum[b1]+str(c1+3)}']))
        b2 = compfinal[0]
        c2 = int(compfinal[1])

        b2 = alphanum.index(b2)
        
        minc = min(int(c1),int(c2))
        maxc = max(int(c1),int(c2))

        minb = min(int(b1),int(b2))
        maxb = max(int(b1),int(b2))
        
        if b1==b2:
            for x in range(minc,maxc+1):
                    if lopp[x][b1] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break
        if c1==c2:
            for x in range(minb,maxb+1):
                    if lopp[c1][x] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break

        if b1==b2 and abs(int(c1)-(int(c2)+1))==4 or b1==b2 and abs((int(c1)+1)-(int(c2)))==4: #or c1==c2 and abs(b1-b2)==5:
            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            
            
            for x in range(minc,maxc+1):
                lopp[x][b1] = 'B'
            break

        elif c1==c2 and abs(b1-b2)==3:
            minb = min(int(b1),int(b2))
            maxb = max(int(b1),int(b2))
            
            for x in range(minb,maxb+1):
                lopp[c1][x] = 'B'
            break

        else:
            print("",end='')

    time.sleep(2)

    print("\nComputer Placing Cruiser: \n")

    while 1<2:
       
        compfirst = (random.choice(['A','B','C','D','E'])+str(random.randint(1,6)))
        b1 = compfirst[0]
        c1 = int(compfirst[1])

        b1 = alphanum.index(b1)

        compfinal = (random.choice([f'{alphanum[b1+2] + str(c1)}',f'{alphanum[b1]+str(c1+2)}']))
        b2 = compfinal[0]
        c2 = int(compfinal[1])

        b2 = alphanum.index(b2)
        minc = min(int(c1),int(c2))
        maxc = max(int(c1),int(c2))

        minb = min(int(b1),int(b2))
        maxb = max(int(b1),int(b2))
        
        if b1==b2:
            for x in range(minc,maxc+1):
                    if lopp[x][b1] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break
        if c1==c2:
            for x in range(minb,maxb+1):
                    if lopp[c1][x] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break

        if b1==b2 and abs(int(c1)-(int(c2)+1))==3 or b1==b2 and abs((int(c1)+1)-(int(c2)))==3: #or c1==c2 and abs(b1-b2)==5:
            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            
            
            for x in range(minc,maxc+1):
                lopp[x][b1] = 'C'
            break

        elif c1==c2 and abs(b1-b2)==2:
            minb = min(int(b1),int(b2))
            maxb = max(int(b1),int(b2))
            
            for x in range(minb,maxb+1):
                lopp[c1][x] = 'C'
            break

        else:
            print("",end='')

    time.sleep(2)

    print("\nComputer Placing Submarine: \n")


    while 1<2:
        
        compfirst = (random.choice(['A','B','C','D','E'])+str(random.randint(1,6)))
        b1 = compfirst[0]
        c1 = int(compfirst[1])

        b1 = alphanum.index(b1)

        compfinal = (random.choice([f'{alphanum[b1+2] + str(c1)}',f'{alphanum[b1]+str(c1+2)}']))
        b2 = compfinal[0]
        c2 = int(compfinal[1])

        b2 = alphanum.index(b2)
        minc = min(int(c1),int(c2))
        maxc = max(int(c1),int(c2))
        minb = min(int(b1),int(b2))
        maxb = max(int(b1),int(b2))
        
        if b1==b2:
            for x in range(minc,maxc+1):
                    if lopp[x][b1] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break
        if c1==c2:
            for x in range(minb,maxb+1):
                    if lopp[c1][x] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break

        if b1==b2 and abs(int(c1)-(int(c2)+1))==3 or b1==b2 and abs((int(c1)+1)-(int(c2)))==3: #or c1==c2 and abs(b1-b2)==5:
            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            
            
            for x in range(minc,maxc+1):
                lopp[x][b1] = 'S'
            break

        elif c1==c2 and abs(b1-b2)==2:
            minb = min(int(b1),int(b2))
            maxb = max(int(b1),int(b2))
            
            for x in range(minb,maxb+1):
                lopp[c1][x] = 'S'
            break

        else:
            print("",end='')

    time.sleep(2)



    print("\nComputer Placing Destroyer: \n")

    while 1<2:
        
        compfirst = (random.choice(['A','B','C','D','E'])+str(random.randint(1,7)))
        b1 = compfirst[0]
        c1 = int(compfirst[1])

        b1 = alphanum.index(b1)

        compfinal = (random.choice([f'{alphanum[b1+2] + str(c1)}',f'{alphanum[b1]+str(c1+1)}']))
        b2 = compfinal[0]
        c2 = int(compfinal[1])

        b2 = alphanum.index(b2)
        minc = min(int(c1),int(c2))
        maxc = max(int(c1),int(c2))
        minb = min(int(b1),int(b2))
        maxb = max(int(b1),int(b2))
        
        if b1==b2:
            for x in range(minc,maxc+1):
                    if lopp[x][b1] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break
        if c1==c2:
            for x in range(minb,maxb+1):
                    if lopp[c1][x] != 'O':
                        print("",end='')
                        b1 = -10
                        c1 = -10
                        break

        if b1==b2 and abs(int(c1)-(int(c2)+1))==2 or b1==b2 and abs((int(c1)+1)-(int(c2)))==2: #or c1==c2 and abs(b1-b2)==5:
            minc = min(int(c1),int(c2))
            maxc = max(int(c1),int(c2))

            
            
            for x in range(minc,maxc+1):
                lopp[x][b1] = 'D'
            break

        elif c1==c2 and abs(b1-b2)==1:
            minb = min(int(b1),int(b2))
            maxb = max(int(b1),int(b2))
            
            for x in range(minb,maxb+1):
                lopp[c1][x] = 'D'
            break

        else:
            print("",end='')
            
    time.sleep(2)


    print("\nComputer Ready\n")

    time.sleep(2)
    #----------------------------------HIT-COUNT-SYSTEM-SETUP-------------------------------------------------------#

    hitonuser = {'A':5,'B':4,'C':3,'D':2,'S':3}
    hitonoppn = {'A':5,'B':4,'C':3,'D':2,'S':3}
    shipnames = {'A':'Aircraft Carrier','B':'Battleship','C':'Cruiser','D':'Destroyer','S':'Submarine'}
    blastedptsuser = []
    blastedptsoppn = []


    #----------------------------------SELECTION-AND-SHIP-BLASTING-CODE-------------------------------------------------------#

    while 1<2:
        buff=0
        player = True
        while buff == 0:
            try:
                i=0
                
                while player == True:
                    i=0 
                    while i == 0:
                        print("\nPlayer's Turn\n")
                        a = input("\nEnter Attack Point: ")
                        if a not in blastedptsuser:
                            blastedptsuser.append(a)
                            i=1
                        else:
                            print('\nPoint already blasted, Try another place\n')

                        
                    b1 = a[0].upper()
                    c1 = int(a[1])
                    b1 = alphanum.index(b1)

                    buffer = lopp[c1][b1]
                    lopp[c1][b1] = 'X'
                    
                        
                        
                    if buffer != 'O' and buffer != 'X':
                        print("\nHIT !\n")
                        time.sleep(2)
                        marker[c1][b1] = 'H'
                        hitonoppn[buffer] -= 1
                        print("\n\nOpponent Board Marker(H is Hit positions, M is Miss positions): \n\n")
                        for x in marker:
                            print(*x)
                        if hitonoppn[buffer] == 0:
                            print("\nComputer's ",shipnames[buffer]," has been SUNK !\n")
                            hitonoppn.pop(buffer)
                            if hitonoppn == {}:
                                time.sleep(3)
                                print("\n\nYou Win !!\n\n")
                                break
                                
                    else:
                        print('\nMISS\n')
                        time.sleep(2)
                        marker[c1][b1] = 'M'
                        player = False
                        buff=1

                    

            except:
                print("\nThat's not allowed, Try Again\n")

        print("\n\nOpponent Board Marker(H is Hit positions, M is Miss positions): \n\n")
        for x in marker:
            print(*x)
            
        time.sleep(2)

        i=0
        j=0
        buffopp=0
        print("\nComputer's Turn\n")
        while buffopp==0:
            i=0
            while i == 0:
                
                a = (random.choice(['A','B','C','D','E','F','G','H','I'])+str(random.randint(1,9)))
                b1 = a[0].upper()
                c1 = int(a[1])

                b1 = alphanum.index(b1)

                if a not in blastedptsoppn:
                    blastedptsoppn.append(a)
                    i=1
                else:
                    print('',end='')

                    
            
                
            b1 = a[0].upper()
            c1 = int(a[1])
            b1 = alphanum.index(b1)

            buffer = l[c1][b1]
            l[c1][b1] = 'X'    
                
            if buffer != 'O' and buffer != 'X':
                print("\nHIT !\n")
                time.sleep(2)
                hitonuser[buffer] -= 1
                buffopp=0
                if hitonuser[buffer] == 0:
                    print("\nYour's ",shipnames[buffer]," has been SUNK !\n")
                    hitonuser.pop(buffer)
                    if hitonuser == {}:
                        time.sleep(3)
                        print("\n\nComputer Wins !!\n\n")
                        print("\nComputer's Board:\n\n")
                        
                        for x in l:
                            print(*x)
                        break
                            
            else:
                print('\nMISS\n')
                time.sleep(2)
                buffopp=1

            print("Your Board:\n\n")
                        
            for x in l:
                print(*x)

    #----------------------------------GAME-END-------------------------------------------------------#

    print('\n\n\nGame Over\n\n\n')
    buffer = input('Press Enter to Continue...')


battleship()
