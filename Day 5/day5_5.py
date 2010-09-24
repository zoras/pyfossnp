wordlist = 'ee ii ee ii oo'

letters = wordlist.split(' ')
for x in letters:
    letter = letters.pop(0)
    letters.append(letter)
    print letters
    