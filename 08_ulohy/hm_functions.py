def get_word():
    """Picks random word from our list in hm_words."""
    import hm_words
    import random
    return random.choice(hm_words.wordlist)

def user_input(tried_chars):
    """Ask user for a single character and checks whether char is right. Returns char."""
    while True:
        guess = input('Skuste uhadnut jedno pismeno zo slova. ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Zadajte len jedno pismeno!')
        elif guess.isalpha() == False:
            print('Zadajte len jedno pismeno!')
        elif guess in tried_chars:
            print('Toto pismeno si uz skusala!')
        else:
            return guess

def show_step(hangman, hidden_word, wrong_char, right_char):
    """Prints hangman picture according to progress of the game (wrong guesses) and hidden word with guesses already made."""
    print(hangman[len(wrong_char)])       
    print('Nespravne uhadnute pismena: {}'.format(wrong_char))
    print()
    field = len(hidden_word) * '-'
    for right in range(len(hidden_word)):
        if hidden_word[right] in right_char:
            field = field[:right] + hidden_word[right] + field[right + 1:]
    for char in field:
        print(char, end=' ')
    print()
