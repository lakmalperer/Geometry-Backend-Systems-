import math

def cross(o, a, b):
    """
    Cross product / orientation test.
    Returns:
        >0 : counterclockwise
        <0 : clockwise
         0 : collinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - \
       (a[1] - o[1]) * (b[0] - o[0])
