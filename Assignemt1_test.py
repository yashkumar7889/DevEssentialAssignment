import unittest
from Assignment1 import SumOfElements

class Test_SumOfElements(unittest.TestCase):

    def test_subArray(self):
        art=SumOfElements()
        self.assertEqual(art.subArray([1,2,1,2], 3),([[1,2], [2,1]],1))
        self.assertEqual(art.subArray([1,2,3],10),([], -1))
    def test_emptyArray(self):
        emptyArray=SumOfElements()
        self.assertRaises(Exception, emptyArray.subArray,[],3)
    def test_invalidArrayElements(self):
        invalidElements=SumOfElements()
        self.assertRaises(ValueError, invalidElements.subArray, [1, 1.2, 4], 5)
        self.assertRaises(ValueError, invalidElements.subArray, [1, "yash", 4], 5)
        

if __name__== '__main__':
    unittest.main()
