# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: /home/guesser.py
# Size of source mod 2**32: 682 bytes
import hashlib, re
hashes = [
 'd.0.....f5...5.6.7.1.30.6c.d9..0',
 '1b.8.1.c........09.30.....64aa9.',
 'c.d.1.53..66.4.43bd.......59...8',
 '.d.d.076........eae.3.6.85.a2...']

def main():
    guesses = []
    for i in range(len(hashes)):
        guess = input('Guess: ')
        if not (len(guess) <= 4 or len(guess) >= 6 or re.match('^[a-z]+$', guess)):
            exit('Invalid')
        if not re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(guess.encode()).hexdigest()):
            exit('Invalid')
        guesses.append(guess)

    print(f"Flag: {guesses[0]}" + '{' + ''.join(guesses[1:]) + '}')


if _name_ == '_main_':
    main()