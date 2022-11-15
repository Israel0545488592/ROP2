from sol import *
import unittest
import doctest


class Tests(unittest.TestCase):

    def test_pattern(self):

        data = '''
    
    	abc-d@mail.com
        abc..def@mail.com
        abc.def@mail.com
        .abc@mail.com
        abc@mail.com
        abc#def@mail.com
        abc_def@mail.com

            '''

        pattern = r'[a-zA-Z]+[\w-]*'  +  r'@g?mail\.' + r'(?:com|org|cc)'

        self.expectation = ['abc-d@mail.com', 'def@mail.com', 'def@mail.com', 'abc@mail.com', 'abc@mail.com', 'def@mail.com', 'abc_def@mail.com']

        self.assertListEqual(re.findall(pattern, data), self.expectation)

def tets_PatternInFile():

    '''
    >>> PatternInFile('binarystring.txt', r'0101', True)
    Ligal:
    0101

    >>> PatternInFile('binarystring.txt', r'0101', False)
    Not Ligal:
    0010101001010000101010100100001010100100101010101001
    1
    00101010101001000000001010101010
    010100100010100101001010
    '''

def test_EmailsInFile():
    
    '''
    >>> EmailsInFile('emails.txt')
    Ligal:
    abc-d@mail.com
    abc@mail.com
    abc_def@mail.com
    israel123@gmail.com
    yonatan56_d@mail.org
    <BLANKLINE>
    Not Ligal:
    abc..def@mail.com
    abc.def@mail.com
    .abc@mail.com
    abc#def@mail.com
    hi05@gmail.stupid
    bibi@mai..com
    111kvn@mail.com
    __kvn@mail.com
    '''


if __name__ == '__main__':

    doctest.testmod(verbose = True)
    unittest.main()