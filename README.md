# wordle-solver
Not a completely automated bot, but helps in solving Wordle quicker.

[words.txt](https://github.com/NiladriMallik/wordle-solver/blob/main/words.txt) and [words2.txt](https://github.com/NiladriMallik/wordle-solver/blob/main/words2.txt) are lists of English words, any of which we could use.

Instructions to use wordle-solver

1. This wordle-solver uses the python library pyautogui to control the keyboard and automatically type in the letters. After executing the program, at times when         pyautogui needs to type in the letters in the wordle window, switch to that window, or else pyautogui will type the words in the terminal itself.
2. After pyautogui types in and attempts to submit one line, switch back to the terminal window and carefully follow the instructions.
3. First python will ask for an input regarding if the word was a invalid, valid but not the correct answer or the correct answer.
4. If the word was invalid, i.e., not in Wordle dictionary, pyautogui will erase the word and enter the next word.
5. If the word was valid but not the correct answer, it will be submitted and then python terminal will ask for input regarding the state of each word.
6. If the word was the correct answer, the terminal will display the word as the final answer.

So, we don't have to type in the words in Wordle, only the input in the terminal, nor think of the words to enter. PyAutoGui and Python will do that, respectively.

**A warning:**
This code does not work as expected most of the time.
