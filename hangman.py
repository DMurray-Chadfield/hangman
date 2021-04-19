word = input('Player one, choose a word: '

word = word.lower()
length = len(word)
guess = '_' * length

while guess != word:
    print(guess)
    letter = input('Player two, guess a letter: ')