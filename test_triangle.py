import math
from triangle import classify_triangle, is_valid_triangle 

#So this is gonna be a test that a triangle with sides 3, 4, and 5 is classified as a right scalene

def test_right_triangle(): 
    assert classify_triangle(3, 4, 5) == "Right Scalene"

# Test that sides 5, 5, and 5 form an equilateral triangle
def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"

 # Test that sides from 5, 5, and 8 form an isosceles triangle now
def test_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"


# Test that sides 4, 5, and 6 form a scalene triangle
def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


# Test that a triangle with a zero-length side is invalid
def test_zero_side_triangle():
    assert classify_triangle(0, 5, 5) == "Invalid"


# Test that sides 1, 2, and 3 form an invalid degenerate triangle
def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


# Test that a triangle with a negative side is invalid
def test_negative_side_triangle():
    assert classify_triangle(-1, 5, 5) == "Invalid"


# Test a right isosceles triangle with a non-integer hypotenuse
def test_right_triangle_non_integer():
    assert classify_triangle(1, 1, math.hypot(1, 1)) == "Right Isosceles"