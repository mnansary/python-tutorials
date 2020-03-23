import unittest
from circles import circle_area
from math import pi
class TestCircleArea(unittest.TestCase):
    def area_test(self):
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(1),0)
        self.assertAlmostEqual(circle_area(1.5),pi*1.5**2)
        
        


    

'''
class TestCir(unittest.TestCase):
    
    
    def test_value(self):
        self.assertRaises(ValueError,cir_area,-2)
        
    def test_type(self):
        self.assertRaises(TypeError,cir_area,2+9j)
        self.assertRaises(TypeError,cir_area,'random')
        self.assertRaises(TypeError,cir_area,True)
'''