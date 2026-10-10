import math
def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True 


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    sides = sorted([a, b, c])
    x, y, z = sides

    if math.isclose(x**2 + y**2, z**2, rel_tol=1e-9):
        triangle_type = "Right " + triangle_type

    return triangle_type


if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(5, 5, 5))
    print(classify_triangle(1, 2, 3))

    