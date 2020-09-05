import re
#dd/mm/yyyy
'''
numberRegex = re.compile(r"(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/([1-2][0-9][0-9][0-9])$")
a = numberRegex.search('12/12/2001')
print(a.group(3))
'''
'''
passwordRegex = re.compile(r'[a-z A-Z]{8,}')
passwordRegex1 = re.compile(r'[1-9]+')
print(passwordRegex.search('abcdefgZ'))
print(passwordRegex1.search('abcdef1Z'))
'''
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
        stripContext = regsp.sub("",context)
        return stripContext

print(strip(stripChar, context))
