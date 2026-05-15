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
        points = sorted(set(points))

        if len(points) <= 1:
            return points
        
        lower = []

        for p in points:
             while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
                lower.append(p)
        
        upper = []

        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)


        return lower[:-1] + upper[:-1]

def hull_perimeter(hull):
     
        n = len(hull)

        if n == 1:
            return 0.0
        
        perimeter = 0.0
        for i in range(n):
        