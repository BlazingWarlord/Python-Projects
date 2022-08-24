#Initialization
def wordle():
    all_words = ["LIGHT","POWER","PIOUS","ALERT","SHOUT","WORDS"]

    removed_letters = []

    yellow_letters = []

    green_letters = []

    import enchant

    dic = enchant.Dict('en_us')

    def word_check(word):
        return dic.check(word)

    def list_print(word,the_list):
        print(word, ' letters :',end='')
        for letter in the_list:
            print(letter,end=' ')
        print()

    import random

    word = random.choice(all_words)

    moves = 1

    f=0

    #Main Logic

    print("Welcome to Wordle: \n")

    while True:
        
        word_input = input("Enter word: ")
        
        if(len(word_input)) != 5:
            print("Retry ! Only 5 letter words...\n")
            
        elif word_check(word_input) != True:
            print("Word doesn't exist...\n")
            
        else:
            word_input = word_input.upper()
            word_split = [chr for chr in word]
            
            for i in range(0,5):
                if(word_input == word):
                    print("You got it...")
                    f=1
                    input("\nPress Enter to Exit...")
                    break
                
                if(word_input[i] == word_split[i]):
                    print("G ",end='')
                    if(word_input[i] not in green_letters):
                        green_letters.append(word_input[i])
                        
                elif(word_input[i] in word_split):
                    print("Y ",end='')
                    if(word_input[i] not in yellow_letters):
                        yellow_letters.append(word_input[i])
                else:
                    print("g ",end='')
                    if(word_input[i] not in removed_letters):
                        removed_letters.append(word_input[i])

                        #G is green; Y is yellow; g is grey
                        
            print("\n")
            
            if(f==1):
                break
            
            list_print("Removed", removed_letters)
            list_print("Yellow", yellow_letters)
            list_print("Green", green_letters)
            print("\n")
            
            if(moves==6):
                print("You are out of moves... Word was ", word)
                break
            
            else:
                moves+=1

            import time
            time.sleep(2)

            

wordle()
