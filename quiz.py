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
def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def convex_hull(points):
        