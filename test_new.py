import unittest
from new import circle_area
from math import pi
class TestCircleArea(unittest.TestCase):
    
    def test_value(self):
        self.assertRaises(ValueError,circle_area,-2)
        
    def test_type(self):
        self.assertRaises(TypeError,circle_area,2+9j)
        self.assertRaises(TypeError,circle_area,'random')
        self.assertRaises(TypeError,circle_area,True)
        
        

if __name__ == '__main__':
    unittest.main()
    

'''
class TestCir(unittest.TestCase):
    
    
   
'''