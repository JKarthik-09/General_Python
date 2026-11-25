"""
===============================================================================
                         PYTHON OPERATORS
===============================================================================

Topic       : Arithmetic Operators & Assignment Operators
Language    : Python
Level       : Beginner to Intermediate
Purpose     : Conceptual Understanding + Practical Implementation

DESCRIPTION:
------------
Operators are special symbols or keywords used to perform operations on
variables and values.

This chapter covers:
    1. Introduction to Operators
    2. Arithmetic Operators
    3. Operator Precedence and Associativity
    4. Assignment Operators
    5. Practical Applications
    6. Common Mistakes
    7. Practice Challenges

LEARNING APPROACH:
------------------
Every concept is explained through:
    - Definition
    - Real-world analogy
    - Syntax
    - Practical implementation
    - Expected output
    - Important observations

===============================================================================
"""


# =============================================================================
# 01. INTRODUCTION TO OPERATORS
# =============================================================================

"""
Imagine that you are running a shopping store.

You have products, prices, quantities, discounts, and a calculator.

You need to:
    - Add the prices of multiple products.
    - Subtract discounts from the total amount.
    - Multiply product prices by their quantities.
    - Divide the total bill among customers.
    - Update the total amount whenever a new purchase is made.

How would you perform these operations programmatically?

This is where OPERATORS come into the picture.

DEFINITION:
-----------
Operators are special symbols or keywords used to perform operations
on variables and values.

The values on which operators perform operations are called OPERANDS.

Example:

    a = 13
    b = 5

    result = a + b

Here:
    a       -> First operand
    +       -> Operator
    b       -> Second operand
    a + b   -> Expression
    18      -> Result


TYPES OF PYTHON OPERATORS:
--------------------------
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

In this chapter, we will concentrate on:

    1. Arithmetic Operators
    2. Assignment Operators

"""


# =============================================================================
# 02. ARITHMETIC OPERATORS
# =============================================================================

"""
DEFINITION:
-----------
Arithmetic operators are used to perform mathematical calculations
between operands.

Think of them as the mathematical tools inside a calculator.

The following operators are covered:

    +       Addition
    -       Subtraction
    *       Multiplication
    /       Division
    //      Floor Division
    %       Modulus
    **      Exponentiation

Let's consider two variables.
"""

a = 13
b = 5


# -----------------------------------------------------------------------------
# 2.1 ADDITION (+)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Adds two operands.

REAL-WORLD ANALOGY:
-------------------
Imagine purchasing two products:

    Product A = Rs. 13
    Product B = Rs. 5

The total amount is Rs. 18.

MATHEMATICAL REPRESENTATION:

    13 + 5 = 18

SYNTAX:

    result = operand1 + operand2

"""

print("\n" + "=" * 65)
print("2.1 ADDITION OPERATOR (+)")
print("=" * 65)

result = a + b

print("First Number  :", a)
print("Second Number :", b)
print("Addition      :", result)

# Expected Output:
# First Number  : 13
# Second Number : 5
# Addition      : 18


# -----------------------------------------------------------------------------
# 2.2 SUBTRACTION (-)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Subtracts the second operand from the first operand.

REAL-WORLD ANALOGY:
-------------------
Imagine that you have Rs. 13.

You purchase something worth Rs. 5.

How much money remains?

    13 - 5 = 8

SYNTAX:

    result = operand1 - operand2
"""

print("\n" + "=" * 65)
print("2.2 SUBTRACTION OPERATOR (-)")
print("=" * 65)

result = a - b

print("First Number  :", a)
print("Second Number :", b)
print("Subtraction   :", result)


# -----------------------------------------------------------------------------
# 2.3 MULTIPLICATION (*)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Multiplies two operands.

REAL-WORLD ANALOGY:
-------------------
Imagine purchasing 5 notebooks.

Each notebook costs Rs. 13.

Instead of adding Rs. 13 five times, we multiply:

    13 * 5 = 65

SYNTAX:

    result = operand1 * operand2
"""

print("\n" + "=" * 65)
print("2.3 MULTIPLICATION OPERATOR (*)")
print("=" * 65)

result = a * b

print("First Number  :", a)
print("Second Number :", b)
print("Multiplication:", result)


# -----------------------------------------------------------------------------
# 2.4 DIVISION (/)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Divides the first operand by the second operand.

REAL-WORLD ANALOGY:
-------------------
Imagine that you have Rs. 13.

You want to distribute the amount equally among 5 people.

Each person receives:

    13 / 5 = 2.6

SYNTAX:

    result = operand1 / operand2

IMPORTANT OBSERVATION:
----------------------
Python's / operator performs TRUE DIVISION.

It returns a floating-point result, even when the division produces
a whole number.

Example:

    10 / 2 = 5.0

NOT:

    10 / 2 = 5

The result is represented as a float.
"""

print("\n" + "=" * 65)
print("2.4 DIVISION OPERATOR (/)")
print("=" * 65)

result = a / b

print("First Number  :", a)
print("Second Number :", b)
print("Division      :", result)
print("Result Type   :", type(result))

# Additional Example

print("\nAdditional Example:")
print("10 / 2 =", 10 / 2)


# -----------------------------------------------------------------------------
# 2.5 FLOOR DIVISION (//)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Performs division and rounds the quotient DOWN to the nearest integer value.

REAL-WORLD ANALOGY:
-------------------
Imagine that you have 13 chocolates.

You want to distribute them equally among 5 children.

Each child receives 2 COMPLETE chocolates.

The remaining chocolates are not considered in the quotient.

    13 // 5 = 2

SYNTAX:

    result = operand1 // operand2

IMPORTANT OBSERVATION:
----------------------
Floor division does not simply remove the decimal portion.

It rounds DOWN towards negative infinity.

Example:

    13 // 5  = 2
    -13 // 5 = -3

Why does -13 // 5 produce -3?

Because:

    -13 / 5 = -2.6

The nearest integer LESS THAN OR EQUAL TO -2.6 is -3.

This distinction is important when working with negative numbers.
"""

print("\n" + "=" * 65)
print("2.5 FLOOR DIVISION OPERATOR (//)")
print("=" * 65)

print("13 // 5  =", 13 // 5)
print("-13 // 5 =", -13 // 5)


# -----------------------------------------------------------------------------
# 2.6 MODULUS (%)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Returns the remainder after division.

REAL-WORLD ANALOGY:
-------------------
You have 13 chocolates.

You distribute them equally among 5 children.

Each child receives 2 chocolates.

How many chocolates remain?

    13 % 5 = 3

MATHEMATICAL REPRESENTATION:

    Dividend = (Divisor * Quotient) + Remainder

    13 = (5 * 2) + 3

SYNTAX:

    result = operand1 % operand2

REAL-WORLD APPLICATION:
-----------------------
One of the most common applications of the modulus operator is
checking whether a number is EVEN or ODD.

An even number always produces a remainder of ZERO when divided by 2.

Example:

    10 % 2 = 0     -> Even
    13 % 2 = 1     -> Odd
"""

print("\n" + "=" * 65)
print("2.6 MODULUS OPERATOR (%)")
print("=" * 65)

result = a % b

print("Remainder of 13 divided by 5:", result)


# Practical Application: Even or Odd

number = 13

if number % 2 == 0:
    print(number, "is an Even Number")
else:
    print(number, "is an Odd Number")


# -----------------------------------------------------------------------------
# 2.7 EXPONENTIATION (**)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Raises the first operand to the power of the second operand.

REAL-WORLD ANALOGY:
-------------------
Imagine a square with a side length of 5 units.

Its area is:

    5 * 5 = 25

Instead of writing repeated multiplication, we can use exponentiation.

    5 ** 2 = 25

Another example:

    2 ** 3 = 2 * 2 * 2 = 8

SYNTAX:

    result = operand1 ** operand2
"""

print("\n" + "=" * 65)
print("2.7 EXPONENTIATION OPERATOR (**)")
print("=" * 65)

print("5 ** 2 =", 5 ** 2)
print("2 ** 3 =", 2 ** 3)


# =============================================================================
# 03. OPERATOR PRECEDENCE AND ASSOCIATIVITY
# =============================================================================

"""
DEFINITION:
-----------
Operator precedence determines which operation is performed first
when an expression contains multiple operators.

REAL-WORLD ANALOGY:
-------------------
Imagine solving a mathematical examination.

You cannot randomly perform mathematical operations.

You follow a specific order of operations.

Python follows a similar hierarchy called OPERATOR PRECEDENCE.

ARITHMETIC OPERATOR PRECEDENCE:
-------------------------------

Priority     Operators                 Description
---------------------------------------------------------------
1            ()                        Parentheses
2            **                        Exponentiation
3            +x, -x                    Unary positive/negative
4            *, /, //, %, @            Multiplication/division group
5            +, -                      Addition/subtraction

IMPORTANT:
----------
The operators *, /, // and % have the SAME precedence.

When they appear together, they are generally evaluated from
LEFT TO RIGHT.

ASSIGNMENT STATEMENTS ARE NOT ANOTHER STEP IN THIS ARITHMETIC
PRECEDENCE LIST.

They follow their own assignment syntax.
"""


# -----------------------------------------------------------------------------
# 3.1 PARENTHESES HAVE HIGHER PRECEDENCE
# -----------------------------------------------------------------------------

print("\n" + "=" * 65)
print("3.1 OPERATOR PRECEDENCE")
print("=" * 65)

result = (10 + 5) * 2

print("(10 + 5) * 2 =", result)

# Evaluation:
#
# (10 + 5) * 2
# 15 * 2
# 30


# -----------------------------------------------------------------------------
# 3.2 EXPONENTIATION BEFORE MULTIPLICATION
# -----------------------------------------------------------------------------

result = 2 + 3 ** 2

print("2 + 3 ** 2 =", result)

# Evaluation:
#
# 2 + (3 ** 2)
# 2 + 9
# 11


# -----------------------------------------------------------------------------
# 3.3 MULTIPLICATION BEFORE ADDITION
# -----------------------------------------------------------------------------

result = 10 + 5 * 2

print("10 + 5 * 2 =", result)

# Evaluation:
#
# 10 + (5 * 2)
# 10 + 10
# 20


# -----------------------------------------------------------------------------
# 3.4 UNDERSTANDING ASSOCIATIVITY
# -----------------------------------------------------------------------------

"""
DEFINITION:
-----------
Associativity determines the evaluation direction when multiple
operators of the SAME precedence appear in an expression.

LEFT-TO-RIGHT ASSOCIATIVITY:

    20 / 5 * 2

Evaluation:

    (20 / 5) * 2
    4.0 * 2
    8.0

RIGHT-TO-LEFT ASSOCIATIVITY:

    2 ** 3 ** 2

Evaluation:

    2 ** (3 ** 2)
    2 ** 9
    512

IMPORTANT:
----------
Most arithmetic operators in the same precedence group are
evaluated from left to right.

Exponentiation is an important exception and is evaluated
from right to left in this example.
"""

print("\nLeft-to-Right:", 20 / 5 * 2)
print("Right-to-Left:", 2 ** 3 ** 2)


# =============================================================================
# 04. ASSIGNMENT OPERATORS
# =============================================================================

"""
DEFINITION:
-----------
Assignment operators are used to assign values to variables or
update the values already stored in variables.

REAL-WORLD ANALOGY:
-------------------
Imagine that you have a wallet containing Rs. 30.

You receive another Rs. 2.

Your updated balance becomes Rs. 32.

Instead of creating a completely new variable to store the updated
balance, you can directly update the existing variable.

This is where ASSIGNMENT OPERATORS become useful.

TYPES COVERED:
--------------

    =       Assignment
    +=      Addition Assignment
    -=      Subtraction Assignment
    *=      Multiplication Assignment
    /=      Division Assignment
    //=     Floor Division Assignment
    %=      Modulus Assignment
    **=     Exponentiation Assignment
"""


# -----------------------------------------------------------------------------
# 4.1 ASSIGNMENT (=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Assigns the value on the RIGHT-HAND SIDE to the variable on the
LEFT-HAND SIDE.

Think of a variable as a labelled storage box.

    balance = 30

The variable 'balance' now refers to the value 30.

IMPORTANT:
----------
The = operator performs assignment.

It does NOT perform comparison.

Comparison is performed using ==.
"""

print("\n" + "=" * 65)
print("4.1 ASSIGNMENT OPERATOR (=)")
print("=" * 65)

balance = 30

print("Initial Balance:", balance)


# -----------------------------------------------------------------------------
# 4.2 ADDITION ASSIGNMENT (+=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Adds a value to the existing variable and assigns the updated result
back to that variable.

REAL-WORLD ANALOGY:
-------------------
Initial wallet balance = Rs. 30

Money received        = Rs. 2

Updated balance       = Rs. 32

SYNTAX:

    balance += 2

EQUIVALENT BASIC EXPRESSION:

    balance = balance + 2
"""

print("\n" + "=" * 65)
print("4.2 ADDITION ASSIGNMENT (+=)")
print("=" * 65)

balance = 30

balance += 2

print("Updated Balance:", balance)


# -----------------------------------------------------------------------------
# 4.3 SUBTRACTION ASSIGNMENT (-=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Subtracts a value from the existing variable and assigns the result.

REAL-WORLD ANALOGY:
-------------------
Initial wallet balance = Rs. 30

Money spent            = Rs. 2

Updated balance        = Rs. 28

EQUIVALENT BASIC EXPRESSION:

    balance = balance - 2
"""

print("\n" + "=" * 65)
print("4.3 SUBTRACTION ASSIGNMENT (-=)")
print("=" * 65)

balance = 30

balance -= 2

print("Updated Balance:", balance)


# -----------------------------------------------------------------------------
# 4.4 MULTIPLICATION ASSIGNMENT (*=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Multiplies the existing variable by a value and assigns the result.

REAL-WORLD ANALOGY:
-------------------
You have 30 boxes.

Each box contains 4 items.

Total items:

    30 * 4 = 120

EQUIVALENT BASIC EXPRESSION:

    items = items * 4
"""

print("\n" + "=" * 65)
print("4.4 MULTIPLICATION ASSIGNMENT (*=)")
print("=" * 65)

items = 30

items *= 4

print("Updated Items:", items)


# -----------------------------------------------------------------------------
# 4.5 DIVISION ASSIGNMENT (/=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Divides the existing variable by a value and assigns the result.

REAL-WORLD ANALOGY:
-------------------
You have Rs. 30.

You divide it equally among 4 people.

Each person receives Rs. 7.5.

EQUIVALENT BASIC EXPRESSION:

    balance = balance / 4

IMPORTANT:
----------
The result of /= is generally a floating-point value.
"""

print("\n" + "=" * 65)
print("4.5 DIVISION ASSIGNMENT (/=)")
print("=" * 65)

balance = 30

balance /= 4

print("Updated Balance:", balance)
print("Result Type:", type(balance))


# -----------------------------------------------------------------------------
# 4.6 FLOOR DIVISION ASSIGNMENT (//=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Performs floor division and assigns the result to the existing variable.

EQUIVALENT BASIC EXPRESSION:

    number = number // 5
"""

print("\n" + "=" * 65)
print("4.6 FLOOR DIVISION ASSIGNMENT (//=)")
print("=" * 65)

number = 13

number //= 5

print("Updated Number:", number)


# -----------------------------------------------------------------------------
# 4.7 MODULUS ASSIGNMENT (%=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Calculates the remainder and assigns it to the existing variable.

EQUIVALENT BASIC EXPRESSION:

    number = number % 5
"""

print("\n" + "=" * 65)
print("4.7 MODULUS ASSIGNMENT (%=)")
print("=" * 65)

number = 13

number %= 5

print("Updated Number:", number)


# -----------------------------------------------------------------------------
# 4.8 EXPONENTIATION ASSIGNMENT (**=)
# -----------------------------------------------------------------------------

"""
PURPOSE:
--------
Raises the existing variable to a specified power and assigns the result.

EQUIVALENT BASIC EXPRESSION:

    number = number ** 2
"""

print("\n" + "=" * 65)
print("4.8 EXPONENTIATION ASSIGNMENT (**=)")
print("=" * 65)

number = 5

number **= 2

print("Updated Number:", number)


# =============================================================================
# 05. PRACTICAL APPLICATIONS
# =============================================================================

"""
Now let's combine the operators we have learned into practical programs.

The objective is to understand how operators work together
in real programming scenarios.
"""


# -----------------------------------------------------------------------------
# 5.1 SHOPPING BILL CALCULATOR
# -----------------------------------------------------------------------------

"""
SCENARIO:
---------
A customer purchases three products.

Product price = Rs. 250
Quantity      = 3
Discount      = Rs. 50

Calculate the final bill.
"""

print("\n" + "=" * 65)
print("5.1 SHOPPING BILL CALCULATOR")
print("=" * 65)

price = 250
quantity = 3
discount = 50

total = price * quantity

total -= discount

print("Product Price:", price)
print("Quantity:", quantity)
print("Discount:", discount)
print("Final Bill:", total)


# -----------------------------------------------------------------------------
# 5.2 EVEN OR ODD NUMBER CHECKER
# -----------------------------------------------------------------------------

"""
SCENARIO:
---------
Determine whether a given number is even or odd.

LOGIC:
------
If a number is divisible by 2 with remainder 0, it is even.

Otherwise, it is odd.
"""

print("\n" + "=" * 65)
print("5.2 EVEN OR ODD CHECKER")
print("=" * 65)

number = 24

if number % 2 == 0:
    print(number, "is EVEN")
else:
    print(number, "is ODD")


# -----------------------------------------------------------------------------
# 5.3 STUDENT MARKS AND AVERAGE CALCULATOR
# -----------------------------------------------------------------------------

"""
SCENARIO:
---------
Calculate the total marks and average marks of a student.
"""

print("\n" + "=" * 65)
print("5.3 STUDENT MARKS CALCULATOR")
print("=" * 65)

maths = 80
physics = 90
chemistry = 70

total_marks = maths + physics + chemistry

average = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average)


# =============================================================================
# 06. COMMON MISTAKES AND IMPORTANT OBSERVATIONS
# =============================================================================

"""
MISTAKE 1: CONFUSING / WITH //

    10 / 3  -> 3.3333333333333335
    10 // 3 -> 3

Remember:
    /  = True Division
    // = Floor Division


MISTAKE 2: CONFUSING = WITH ==

    number = 10

    Here, = assigns a value.

    number == 10

    Here, == compares two values and returns True or False.


MISTAKE 3: DIVIDING BY ZERO

    10 / 0

This produces a ZeroDivisionError.

Division, floor division and modulus with a zero divisor are
not permitted.


MISTAKE 4: MISUNDERSTANDING FLOOR DIVISION

    13 // 5  = 2
    -13 // 5 = -3

Floor division rounds towards negative infinity.
It does not simply remove the decimal portion.


MISTAKE 5: IGNORING OPERATOR PRECEDENCE

    10 + 5 * 2 = 20

    (10 + 5) * 2 = 30

Parentheses can change the evaluation order.
"""


# =============================================================================
# 07. QUICK REFERENCE
# =============================================================================

"""
ARITHMETIC OPERATORS
--------------------

Operator    Name                Example         Result
-------------------------------------------------------
+           Addition             13 + 5          18
-           Subtraction          13 - 5          8
*           Multiplication       13 * 5          65
/           Division             13 / 5          2.6
//          Floor Division       13 // 5         2
%           Modulus              13 % 5          3
**          Exponentiation       5 ** 2          25


ASSIGNMENT OPERATORS
--------------------

Operator    Equivalent Expression       Purpose
-------------------------------------------------------
=           -                           Assignment
+=          x = x + y                   Addition
-=          x = x - y                   Subtraction
*=          x = x * y                   Multiplication
/=          x = x / y                   Division
//=         x = x // y                  Floor Division
%=          x = x % y                   Modulus
**=         x = x ** y                  Exponentiation

"""


# =============================================================================
# 08. PRACTICE CHALLENGES
# =============================================================================

"""
IMPORTANT:
----------
Try solving these challenges WITHOUT executing the code first.

Predict the output, understand the logic, and then execute the program
to verify your understanding.


CHALLENGE 1: PREDICT THE OUTPUT
-------------------------------

a = 15
b = 4

print(a / b)
print(a // b)
print(a % b)
print(a ** b)


CHALLENGE 2: OPERATOR PRECEDENCE
--------------------------------

result = 10 + 5 * 2 ** 2 - 5

print(result)


CHALLENGE 3: ASSIGNMENT OPERATORS
---------------------------------

x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x)


CHALLENGE 4: BUILD YOUR OWN CALCULATOR
--------------------------------------

Create a Python program that:

1. Accepts two numbers from the user.
2. Performs addition.
3. Performs subtraction.
4. Performs multiplication.
5. Performs division.
6. Performs floor division.
7. Finds the remainder.
8. Calculates the power.

BONUS:
------
Add appropriate validation to prevent division by zero.

"""


# =============================================================================
# 09. FINAL TAKEAWAY
# =============================================================================

"""
Understanding operators is not just about memorizing symbols.

It is about understanding:

    - How Python evaluates expressions.
    - How mathematical calculations are performed.
    - How variables store and update values.
    - How different operations work together in practical programs.

REMEMBER:

    ARITHMETIC OPERATORS
        -> Perform mathematical calculations.

    ASSIGNMENT OPERATORS
        -> Assign or update variable values.

Master these fundamentals before moving towards:

    1. Comparison Operators
    2. Logical Operators
    3. Bitwise Operators
    4. Membership Operators
    5. Identity Operators

===============================================================================
                         HAPPY CODING! 🐍
===============================================================================
"""