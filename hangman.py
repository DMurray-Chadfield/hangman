word = input('Player one, choose a word: ')

word = word.lower()
length = len(word)
guess = '_' * length

def find_all(string, letter):
    indices = []
    index = string.find(letter)
    while index != -1:
        indices.append(index)
        string = string.replace(letter, '-', 1)
        index = string.find(letter)
    return indices



while guess != word:
    print(guess)
    letter = input('Player two, guess a letter: ')
