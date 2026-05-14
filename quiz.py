import math

# -----------------------------------
# Point Utilities
# -----------------------------------

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
    """
    Euclidean distance between two points.
    """
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


# -----------------------------------
# Convex Hull (Andrew's Monotone Chain)
# -----------------------------------

def convex_hull(points):
    """
    Returns points on the convex hull
    in counterclockwise order.
    """

    # Remove duplicates and sort
    points = sorted(set(points))

    # Special case
    if len(points) <= 1:
        return points

    # Build lower hull
    lower = []

    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []

    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Remove duplicate endpoints
    return lower[:-1] + upper[:-1]


# -----------------------------------
# Perimeter Calculation
# -----------------------------------

def hull_perimeter(hull):
    """
    Computes perimeter of convex hull.
    """

    n = len(hull)

    if n == 1:
        return 0.0

    perimeter = 0.0

    for i in range(n):
        perimeter += distance(hull[i], hull[(i + 1) % n])

    return perimeter


# -----------------------------------
# Main Program
# -----------------------------------

def main():
    n = int(input())

    points = []

    for _ in range(n):
        x1, y1, x2, y2 = map(float, input().split())

        # Generate all 4 corners
        points.append((x1, y1))
        points.append((x1, y2))
        points.append((x2, y1))
        points.append((x2, y2))

    # Compute convex hull
    hull = convex_hull(points)

    # Compute perimeter
    perimeter = hull_perimeter(hull)

    # Output with precision
    print(f"{perimeter:.6f}")


if __name__ == "__main__":
    main()