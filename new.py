from math import pi
def circle_area(r):
    '''
    This function does this......
    asdkjahsjdhjkas
    asjdkjas
    '''
    if r<0:
        raise ValueError("negative number not supported")
    if type(r) not in [int,float]:
        raise TypeError('Type not supported')

    return pi*r**2

circle_area()