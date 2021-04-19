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


used_letters = []
while guess != word:
    print(guess, used_letters)
    letter = input('Player two, guess a letter: ')
    used_letters.append(letter)
    indices = find_all(word, letter)
    if len(indices) == 0:
        print('Incorrect, try again!')
    else:
        print('Correct')
        for i in indices:
            guess[i] = letter