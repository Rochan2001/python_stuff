import re
stripChar = input('Enter character to strip: ')
context = input('Enter string to strip: ')
stripContext = None

def strip(char, string):
    if char == "":
        regsp = re.compile(r'^\s+|\s+$')
        stripContext = regsp.sub("", context)
        return stripContext
    else:
        regsp = re.compile(r'^{}+|{}+$'.format(char, char))
        stripContext = regsp.sub("", context)
        return stripContext


print(strip(stripChar, context))
