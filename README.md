## Triangle Classifier

Project Description

This project is a Python triangle classifier created for my CSC 325 Software Engineering assignment.

The program accepts three side lengths and determines whether they form a valid triangle. If the triangle is valid, the program classifies it as Equilateral, Isosceles, or Scalene.

The program also checks whether a triangle has a right angle using the Pythagorean theorem and a floating-point tolerance. If the sides do not form a valid triangle, the program returns "Invalid".

 How to Run the Tests

1. Open the TriangleClassifier folder in Visual Studio Code.

2. Open the terminal.

3. Install the required package:

python -m pip install -r requirements.txt

4. Running all tests:

python -m pytest -v

The project contains eight unit tests and one acceptance test.



#Equivalence Classes and Boundary Cases

Equivalence classes are groups of inputs that should behave the same way.

For this assignment, I identified the following classes:

1. Equilateral: All three sides are equal, such as (5, 5, 5).

2. Isosceles: Exactly two sides are equal, such as (5, 5, 8).

3. Scalene: All three sides are different, such as (4, 5, 6).

4. Right Triangle: The sides satisfy the Pythagorean theorem, such as (3, 4, 5).

5. Invalid Triangle: The side lengths cannot form a valid triangle.


#Boundary Cases

1. Zero-length side: (0, 5, 5) must return "Invalid".

2. Negative side: (-1, 5, 5) must return "Invalid".

3. Degenerate triangle: (1, 2, 3) must return "Invalid" because 1 + 2 = 3.

4. Non-integer right triangle: (5, 5, 5 × sqrt(2) etc) must return "Right Isosceles". This checks that the program handles floating-point calculations correctly.

#Why an Equilateral Triangle Cannot Be Right-Angled?

So an equilateral triangle has three equal angles of 60 degrees. A right triangle must have one angle of 90 degrees, so an equilateral triangle cannot also be a right triangle.




## Copilot Review Log

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_equilateral_triangle | Yes | Kept | Verified that (5, 5, 5) returns Equilateral. |
| test_isosceles_triangle | Yes | Kept | Verified that (5, 5, 8) has exactly two equal sides. |
| test_scalene_triangle | Yes | Kept | Verified that (4, 5, 6) has three different sides. |
| test_zero_side_triangle | Yes | Edited | [Describe what you actually changed.] |
| test_right_triangle_non_integer | Yes | [Your decision] | [Explain how you checked floating-point tolerance.] |


## Acceptance Criteria

1. Valid triangles: [State the input and expected classification.]
2. Invalid triangles: [State what should happen for unbuildable side lengths.]
3. Right triangles: [State how the program identifies pieces requiring reinforced corners.]

## AI-Use Disclosure

I did use GitHub Copilot in Visual Studio Code to help generate suggestions for my pytest unit tests. But at the same time, I also reviewed the suggestions and checked them against the assignment requirements instead of accepting them without checking.

I also use ChatGPT for step-by-step guidance on setting up the project, mostly for the early parts of this assignment, with assistance including, understanding Python code, double-checking said code, troubleshooting, and organizing the README. I verified the program by running pytest and checking the test results.

And lastly I reviewed the acceptance test against the customer's requirements and documented the AI assistance I received during that part of the assignment. And that's should be everything.