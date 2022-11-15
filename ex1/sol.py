from os.path import isfile
import re

'''
    PatternInFile searches for lines that match a regex in a text file.
    EmailsInFile does so for email format using PatternInFile,
    it prints a list of ligal email addresses and another of nonligal.
'''

def PatternInFile(dir: str, pattern: str, asPattern: bool = True):

    if not isfile(dir): raise FileNotFoundError(dir + ' can not be found')

    if asPattern:   print('Ligal:')
    else:           print('Not Ligal:')
    
    with open(dir, 'r') as f:
        for line in f:

            match = re.fullmatch(pattern, line.rstrip())
            if match is not None and asPattern: print(line.rstrip())
            if match is None and not asPattern: print(line.rstrip())


def EmailsInFile(dir: str):

    ligal_format = r'[a-zA-Z]+[\w-]*'  +  r'@g?mail\.'  +  r'(?:com|org|cc)' + r'$'

    PatternInFile(dir, ligal_format, True)
    print()
    PatternInFile(dir, ligal_format, False)