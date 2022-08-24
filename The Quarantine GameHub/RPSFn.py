def rps():
    import random
    import time

    scores = {'You':0,'Computer':0}

    n = int(input('How many rounds do you want to play: '))

    for x in range(n):

        print('\nRound - ',x+1)
        time.sleep(2)

        #For simplicity, lets assume 1 is rock, 2 is paper and 3 is scissors

        choices = ['Rock','Paper','Scissors']

        while True:
            userchoice = int(input("\nEnter 1 for Rock, 2 for Paper and 3 for Scissors: "))
            if userchoice not in [1,2,3]:
                print("\nThat is an invalid input\n")
            else:
                break


        cpuchoice = random.choice([1,2,3])


        if userchoice == cpuchoice:
            print(f"\nDraw, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")

        elif userchoice == 1 and cpuchoice == 2:
            print(f"\nComputer Wins, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['Computer'] += 1

        elif userchoice == 1 and cpuchoice == 3:
            print(f"\nYou Win, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['You'] += 1

        elif userchoice == 2 and cpuchoice == 1:
            print(f"\nYou Win, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['You'] += 1

        elif userchoice == 2 and cpuchoice == 3:
            print(f"\nComputer Wins, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['Computer'] += 1

        elif userchoice == 3 and cpuchoice == 1:
            print(f"\nComputer Wins, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['Computer'] += 1

        elif userchoice == 3 and cpuchoice == 2:
            print(f"\nYou Win, You put {choices[userchoice-1]} and Computer put {choices[cpuchoice-1]}\n")
            scores['You'] += 1

        time.sleep(2)

    print(f"\nFINAL SCORES:\n\nYou: {scores['You']}\nComputer: {scores['Computer']}")
    time.sleep(2)
    input('\n\nPress Enter to Exit')

rps()
