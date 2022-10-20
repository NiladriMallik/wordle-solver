import pyautogui
from time import sleep

'''
Number corresponding to the color/state of each box
-1 -> Empty
0  -> Gray
1  -> Yellow
2  -> Green
'''

'''
Color corresponding to the state of the word of each line after pressing enter
0 -> invalid word
1 -> valid word, but not correct
2 -> correct word
'''
#row will contain the states of all the five boxes of each line.
#the state of each box will be in the format [state,letter]

# global wordList

with open('words2.txt') as file:
    wordList=file.read().splitlines()




wordList=[z.upper() for z in wordList if "'" not in z and " " not in z and len(z)==5]

print('List of words imported')

print(len(wordList))
# print(wordList)
# quit()

#state will contain 0, 1 or 2, corresponding to whether the word is invalid, valid but incorrect or the correct word
state=0


start=input("Ready to begin: Y/N:\t")

row=[[-1,''],[-1,''],[-1,''],[-1,''],[-1,'']]
word='AUDIO'

if start.lower()=='y':
    print("your response was "+start+'.')
    print("Typing the word now. Switch to the other window...")
    sleep(3)
    while(state!=2):
        
        #write the word to wordle screen
        pyautogui.write(word,interval=0.25)
        pyautogui.press('enter')
        sleep(1)
        state=int(input("Switch to this window. Is the word valid? 0=invalid, 1=valid but incorrect, 2=correct: "))
        
        #if word is invalid
        if(state==0):
            print("Typing the next word now. Switch to the other window...")
            sleep(3)
            for i in range(5):
                pyautogui.press('backspace')
            # pyautogui.write(wordList[0],interval=0.25)
            # pyautogui.press('enter')
            wordList.remove(word)
            print(f"Words in wordlist: {len(wordList)}")
            if not wordList:
                break
            word=wordList[0]
            continue
            
        #if word is valid but not the correct answer    
        elif state==1:
            # sleep(2)
            # print(row)
            for i in range(len(row)):
                row[i][0]=int(input("State of the {} index letter: 0=Gray, 1=Yellow, 2=Green:\t".format(i)))
                row[i][1]=word[i]
                
                if row[i][0]==0:
                    #keep only those words that do not have the letter
                    wordList=[k for k in wordList if row[i][1] not in k]
                    # print(wordList)
                    continue
                elif row[i][0]==1:
                    #keep only those words that have the letter but in another position
                    wordList=[k for k in wordList if row[i][1] in k and row[i][1]!=k[i]]
                    # print(wordList)
                    continue
                elif row[i][0]==2:
                    #keep only those words
                    wordList=[k for k in wordList if row[i][1]==k[i]]
                    # print(wordList)
                    
                    continue
            # print(row)
            if word in wordList:
                wordList.remove(word)
                
            print(f"Words in wordlist: {len(wordList)}")
            
            if not wordList:
                break
            word=wordList[0]
            print("Typing the next word now. Switch to the other window...")
            sleep(2)
            continue
        #if word is the correct answer
        else:
            state=2

if state==2:
    print("So, the correct answer is: {}".format(word))
else:
    print("My apologies, better luck next time!")