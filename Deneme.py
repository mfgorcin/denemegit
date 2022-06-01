

from dataclasses import replace


def DifferentCases(str): 
    newStr = ''
    finalWord = []
    
    for char in str:
        if char.isalpha():
            newStr += char
        else:
            newStr += ' '
            
    for word in newStr.split():
        word = word.replace(word[0], word[0].upper())
        word = word.replace(word[1:len(word)], word[1:len(word)].lower())
        finalWord.append(word)
        
    return ''.join(finalWord)


#print(val2.title())      # Kelimenin ilk harfi büyük