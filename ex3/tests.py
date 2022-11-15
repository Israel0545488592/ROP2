from sol import *
import unittest


class Tests(unittest.TestCase):

    def test_build(self):

        self.assertEqual(type(l), MyList)
        self.assertEqual(len(l), 7)
        
    def test_repr(self):
        
        self.assertEqual(l.__repr__(), '[[[1, 2], [12.3, \'hi there\'], [(1, 2, {2: <class \'int\'>}), -12]], [[11, 0, 0.0], [2, set()]], [[[[\'hi again\']]]], 1, 2, 3, 4]')

    def test_get(self):
        
        self.assertEqual(l[0, 0, 1], 2)
        self.assertEqual(l[3:], [1, 2, 3, 4])
        self.assertEqual(l[0, 2, :], [(1, 2, {2 : int}), -12])
        self.assertEqual(l[1:, 0, 0, -2:], [0, 0.])
        self.assertEqual(l[-5: -2, 0, 0, 0, 0, 0], 'hi again')
        self.assertEqual(l[1::2], [[[11, 0, 0.], [2, set()]], 1, 3])

    def test_set(self):
        
        l[0] = 5
        self.assertEqual(l[0:2], [5, [[11, 0, 0.0], [2, set()]]])
        l[2] = 'I am tired'
        self.assertEqual(l[-1:0:-2], [4, 2, 'I am tired'])
        l[1, 1, 1] = {}
        self.assertEqual(l[1, 1, 1], {})

if __name__ == '__main__':

    l = MyList([[[1, 2], [12.3, 'hi there'], [(1, 2, {2 : int}), -12]], [[11, 0, 0.], [2, set()]], [[[['hi again']]]], 1, 2, 3, 4])

    unittest.main()

