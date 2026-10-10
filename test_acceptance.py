from triangle import classify_triangle


def test_stained_glass_requirements():
    # We need to check that a valid triangle is classified correctly
    assert classify_triangle(5, 5, 5) == "Equilateral"

    # Same thing we need to check that an invalid triangle returns the correct message
    assert classify_triangle(1, 2, 3) == "Invalid"

    # finally check the right triangle is flagged for reinforced corners
    assert classify_triangle(3, 4, 5) == "Right Scalene"