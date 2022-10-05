#Import Necessary Modules 

import enchant

dic = enchant.Dict('en_us')

#Open the text file 

f = open('Test.txt','r')

text = f.read()

#Clean the text 

def string_cleaner(text):

    text_wo_nl = text.replace('\n',' ') #Remove all escape sequences

    text_wo_spe_chrs = ''

    for char in text_wo_nl:
        
        if char.isalpha() != True and char != ' ': #Remove all non-alphabet characters
            
            text_wo_spe_chrs+=' '
            
        else:
            
            text_wo_spe_chrs += char

    return text_wo_spe_chrs
        

words = string_cleaner(text).split(' ')

#Check whether word exists in Dictionary

for word in words:
    if word.isalpha() == True and dic.check(word) != True:
        print(word + ' is wrong. Suggestions: ',end = '')
        possible_words = dic.suggest(word)
        print(*possible_words)
        print('\n')
