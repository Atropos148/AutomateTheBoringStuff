#! python3

import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code(optional)
    (\s|-|\.)?  # separator
    (\d{3}) # first 3 numbers
    (\s|-|\.) # separator
    (\d{4}) # last 4 numbers
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension(optional)
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
