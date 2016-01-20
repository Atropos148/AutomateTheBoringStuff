#! python3
# bulletPointAdder.py - adds Wikipedia bullet points to the start
# of each line of tex in clipboard

import pyperclip


text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # add star to each string

text = '\n'.join(lines)
pyperclip.copy(text)
