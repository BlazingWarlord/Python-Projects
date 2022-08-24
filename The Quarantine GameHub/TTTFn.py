def tictactoe():
    from os import name,system
    def clear(): 
  
        if name == 'nt': 
            _ = system('cls') 
      
        else: 
            _ = system('clear')
        
    d = {'X':0,'O':0}

    import time
    import random
    n = int(input("How many matches do you want to play ?: "))

    for x in range(1,n+1):
        board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]

        print("\nRound ",x)
        while 1 < 2:
            
            while 1<2:
                userplayrow = int(input("\nEnter Row (--->): "))
                userplaycolumn = int(input("\nEnter Column (\/): "))
                if board[userplayrow-1][userplaycolumn-1] == '-':
                    board[userplayrow-1][userplaycolumn-1] = 'X'
                    break
                else:
                    print("\nSorry, Non-Empty Space, Try Again")
                    
                    

            #ROWS 

            if board[0][0] == board[0][1] == 'O' and board[0][2] == '-':
                board[0][2] = 'O'
                

            elif board[0][1] == board[0][2] == 'O' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[0][2] == 'O' and board[0][1] == '-':
                board[0][1] = 'O'


            elif board[1][0] == board[1][1] == 'O' and board[1][2] == '-':
                board[1][2] = 'O'

            elif board[1][1] == board[1][2] == 'O' and board[1][0] == '-':
                board[1][0] = 'O'

            elif board[1][0] == board[1][2] == 'O' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[2][0] == board[2][1] == 'O' and board[2][2] == '-':
                board[2][2] = 'O'

            elif board[2][1] == board[2][2] == 'O' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[2][0] == board[2][2] == 'O' and board[2][1] == '-':
                board[2][1] = 'O'


            #COLUMNS    

            elif board[1][0] == board[2][0] == 'O' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[2][0] == 'O' and board[1][0] == '-':
                board[1][0] = 'O'

            elif board[1][0] == board[0][0] == 'O' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[1][1] == board[2][1] == 'O' and board[0][1] == '-':
                board[0][1] = 'O'

            elif board[0][1] == board[2][1] == 'O' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[1][1] == board[0][1] == 'O' and board[2][1] == '-':
                board[2][1] = 'O'

            elif board[1][2] == board[2][2] == 'O' and board[0][2] == '-':
                board[0][2] = 'O'

            elif board[0][2] == board[2][2] == 'O' and board[1][2] == '-':
                board[1][2] = 'O'

            elif board[1][2] == board[0][2] == 'O' and board[2][2] == '-':
                board[2][2] = 'O'

            #DIAGONALS

            elif board[0][0] == board[1][1] == 'O' and board[2][2] == '-':
                board[2][2] = 'O'

            elif board[1][1] == board[2][2] == 'O' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[2][2] == 'O' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[0][2] == board[1][1] == 'O' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[0][2] == board[2][0] == 'O' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[1][1] == board[2][0] == 'O' and board[0][2] == '-':
                board[0][2] = 'O'


            elif board[0][0] == board[0][1] == 'X' and board[0][2] == '-':
                board[0][2] = 'O'
                

            elif board[0][1] == board[0][2] == 'X' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[0][2] == 'X' and board[0][1] == '-':
                board[0][1] = 'O'


            elif board[1][0] == board[1][1] == 'X' and board[1][2] == '-':
                board[1][2] = 'O'

            elif board[1][1] == board[1][2] == 'X' and board[1][0] == '-':
                board[1][0] = 'O'

            elif board[1][0] == board[1][2] == 'X' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[2][0] == board[2][1] == 'X' and board[2][2] == '-':
                board[2][2] = 'O'

            elif board[2][1] == board[2][2] == 'X' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[2][0] == board[2][2] == 'X' and board[2][1] == '-':
                board[2][1] = 'O'


            #COLUMNS    

            elif board[1][0] == board[2][0] == 'X' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[2][0] == 'X' and board[1][0] == '-':
                board[1][0] = 'O'

            elif board[1][0] == board[0][0] == 'X' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[1][1] == board[2][1] == 'X' and board[0][1] == '-':
                board[0][1] = 'O'

            elif board[0][1] == board[2][1] == 'X' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[1][1] == board[0][1] == 'X' and board[2][1] == '-':
                board[2][1] = 'O'

            elif board[1][2] == board[2][2] == 'X' and board[0][2] == '-':
                board[0][2] = 'O'

            elif board[0][2] == board[2][2] == 'X' and board[1][2] == '-':
                board[1][2] = 'O'

            elif board[1][2] == board[0][2] == 'X' and board[2][2] == '-':
                board[2][2] = 'O'

            #DIAGONALS

            elif board[0][0] == board[1][1] == 'X' and board[2][2] == '-':
                board[2][2] = 'O'

            elif board[1][1] == board[2][2] == 'X' and board[0][0] == '-':
                board[0][0] = 'O'

            elif board[0][0] == board[2][2] == 'X' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[0][2] == board[1][1] == 'X' and board[2][0] == '-':
                board[2][0] = 'O'

            elif board[0][2] == board[2][0] == 'X' and board[1][1] == '-':
                board[1][1] = 'O'

            elif board[1][1] == board[2][0] == 'X' and board[0][2] == '-':
                board[0][2] = 'O'

            else:
                a = 0
                for i in range(0,3):
                    for j in range(0,3):
                        if board[i][j] == '-':
                            a+=1
                if a==0:
                    print("Draw")
                    time.sleep(5)
                    break
                while 1<2:
                    opprow = random.choice([0,1,2])
                    oppcolumn = random.choice([0,1,2])
                    if board[opprow][oppcolumn] == '-':
                        board[opprow][oppcolumn] = 'O'
                        break
                    
            for i in board:
                print(*i)
                

            #WINS

            if board[0][0] == board[0][1] == board[0][2] == 'X' or board[0][0] == board[0][1] == board[0][2] == 'O':
                print(board[0][0]," Wins")
                d[board[0][0]]+=1
                time.sleep(5)
                break
                

            elif board[1][0] == board[1][1] == board[1][2] == 'X' or board[1][0] == board[1][1] == board[1][2] == 'O':
                print(board[1][0]," Wins")
                d[board[1][0]]+=1
                time.sleep(5)
                break
            
            elif board[2][0] == board[2][1] == board[2][2] == 'X' or board[2][0] == board[2][1] == board[2][2] == 'O'  :
                print(board[2][0]," Wins")
                d[board[2][0]]+=1
                time.sleep(5)
                break
            
            elif board[0][0] == board[1][0] == board[2][0] == 'X' or board[0][0] == board[1][0] == board[2][0] == 'O' :
                print(board[2][0]," Wins")
                d[board[2][0]]+=1
                time.sleep(5)
                break
            
            elif board[0][1] == board[1][1] == board[2][1] == 'X' or board[0][1] == board[1][1] == board[2][1] == 'O':
                print(board[2][1]," Wins")
                d[board[2][1]]+=1
                time.sleep(5)
                break
            
            elif board[0][2] == board[1][2] == board[2][2] == 'X' or board[0][2] == board[1][2] == board[2][2] == 'O':
                print(board[2][2]," Wins")
                d[board[2][2]]+=1
                time.sleep(5)
                break
            
            elif board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'O':
                print(board[2][2]," Wins")
                d[board[2][2]]+=1
                time.sleep(5)
                break
            
            elif board[0][2] == board[1][1] == board[2][0] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'O':
                print(board[2][0]," Wins")
                d[board[2][0]]+=1
                time.sleep(5)
                break

    print(f"\nSCORES: \n\nX : {d['X']}\nO : {d['O']}")
    time.sleep(3)
    if d['X'] > d['O']:
        print("\nX Wins")
        time.sleep(5)
    elif d['X'] < d['O']:
        print("\nO Wins")
        time.sleep(5)
    else:
        print("\nDraw")

    clear()
            
       
tictactoe()                  

