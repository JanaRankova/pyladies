import hm_words
import hm_stickman
import hm_functions

hidden_word = hm_functions.get_word()
hangman = hm_stickman.hangman
right_char = ''
wrong_char = ''

def evaluate():
    """Shows when player wins + number of guesses."""
    if len(wrong_char) > 4:
        print('Gratulujem, vyhrala si hru so slovom {}. Spravila si {}. nespravnych pokusov.'.format(hidden_word, len(wrong_char)))
    elif len(wrong_char) >1:
        print('Gratulujem, vyhrala si hru so slovom {}. Spravila si {}. nespravne pokusy.'.format(hidden_word, len(wrong_char)))
    else:
        print('Gratulujem, vyhrala si hru so slovom {}. Spravila si {}. nespravny pokus.'.format(hidden_word, len(wrong_char)))

while True:
    hm_functions.show_step(hangman, hidden_word, wrong_char, right_char)
    guess = hm_functions.user_input(wrong_char + right_char)
    if guess in hidden_word:
        right_char = right_char + guess
        got_them = True
        for char in range(len(hidden_word)):
            if hidden_word[char] not in right_char:
                got_them = False
        if got_them:
            evaluate()
            break
    else:
        wrong_char = wrong_char + guess
        if len(wrong_char) == 9:
            print(hangman[9])
            print('Prehral si po', len(right_char) + len(wrong_char), 'kolach!')
            break
