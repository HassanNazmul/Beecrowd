# Path: 1001 Extremely Basic.py
# Read two integer values, in this case, the variables A and B.
import math
A = int(input())
B = int(input())

X = A + B

print("X = %d" % X)

# ]=========================================================================================================================[#

# Path: 1002 Area of a Circle.py
# Read the value of the radius of a circle, R, and calculate the area of the circle,
# considering that A = π . R2. Use 3.14159 as the value of π.

R = float(input())

A = 3.14159 * R * R

print("A=%.4f" % A)

# ]=========================================================================================================================[#

# Path: 1003 Simple Sum.py
# Read two integer values, in this case, the variables A and B.
# After this, calculate the sum between them and assign it to the variable SOMA.
# Print the result like the example below.

A = int(input())
B = int(input())

SOMA = A + B

print("SOMA = %d" % SOMA)

# ]=========================================================================================================================[#

# Path: 1004 Simple Product.py
# Read two integer values. After this, calculate the product between them and store the result in a variable named PROD.
# Print the result like the example below. Do not forget to print the end of line after the result, otherwise you will receive “Presentation Error”.

A = int(input())
B = int(input())

PROD = A * B

print("PROD = %d" % PROD)

# ]=========================================================================================================================[#

# Path: 1005 Average 1.py
# Read two floating points' values of double precision A and B, corresponding to two student's grades.
# After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5.
# Each grade can be from zero to ten, always with one decimal place.

A = float(input())
B = float(input())

MEDIA = (A * 3.5 + B * 7.5) / 11

print("MEDIA = %.5f" % MEDIA)

# ]=========================================================================================================================[#

# Path: 1006 Average 2.py
# Read three values (variables A, B and C), which are the three student's grades.
# Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5.
# Consider that each grade can go from 0 to 10.0, always with one decimal place.

A = float(input())
B = float(input())
C = float(input())

MEDIA = (A * 2 + B * 3 + C * 5) / 10

print("MEDIA = %.1f" % MEDIA)

# ]=========================================================================================================================[#

# Path: 1007 Difference.py
# Read four integer values named A, B, C and D.
# Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = A * B - C * D

print("DIFERENCA = %d" % DIFERENCA)

# ]=========================================================================================================================[#

# Path: 1008 Salary.py
# Read an employee's number, his/her worked hours number in a month and the amount he received per hour.
# Calculate and print the employee's total salary that he/she will receive at end of the month, with two decimal places.

NUMBER = int(input())
HOURS = int(input())
SALARY = float(input())

TOTAL = HOURS * SALARY

print("NUMBER = %d" % NUMBER)
print("SALARY = U$ %.2f" % TOTAL)

# ]=========================================================================================================================[#

# Path: 1009 Salary with Bonus.py
# Read the name of a seller.
# Read his/her fixed salary.
# Read the total sold by him/her in the month (in money).
# Calculate and print the final salary (total) of this seller at the end of the month, with two decimal places.

NAME = input()
SALARY = float(input())
TOTAL = float(input())

TOTAL = SALARY + TOTAL * 0.15

print("TOTAL = R$ %.2f" % TOTAL)

# ]=========================================================================================================================[#

# Path: 1010 Simple Calculate.py
# Read two integer values, in this case, the variables A and B.
# After this, calculate the product between them and assign it to the variable PROD.
# Print the result like the example below.

A = input().split()
B = input().split()

CODE1, UNIT1, PRICE1 = A
CODE2, UNIT2, PRICE2 = B

TOTAL = (int(UNIT1) * float(PRICE1)) + (int(UNIT2) * float(PRICE2))

print("VALOR A PAGAR: R$ %.2f" % TOTAL)

# ]=========================================================================================================================[#

# Path: 1011 Sphere.py
# Read the radius value of a sphere, calculate and print its volume.
# The formula to calculate the volume is: (4/3) * pi * R3.
# Consider (assign) for pi the value 3.14159.
# Consider (do not forget to use) the power 3.

R = float(input())

VOLUME = (4/3) * 3.14159 * R * R * R

print("VOLUME = %.3f" % VOLUME)

# ]=========================================================================================================================[#

# Path: 1012 Area.py
# Read three floating point numbers (double precision A, B and C), representing the sides of a triangle.
# Calculate and print the area of the triangle, considering that the formula to calculate the area of a triangle is: area = (A + B) * C / 2.
# Consider the value of pi = 3.14159.

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * C * C
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B * B
RETANGULO = A * B

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)

# ]=========================================================================================================================[#

# Path: 1013 The Greatest.py
# Read three integer values and present the greatest one followed by the message “eh o maior” (is the greatest).
# Use the following formula: greatest = (a + b + abs(a-b)) / 2

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

MAIORAB = (A + B + abs(A - B)) / 2
MAIOR = (MAIORAB + C + abs(MAIORAB - C)) / 2

print("%d eh o maior" % MAIOR)

# ]=========================================================================================================================[#

# Path: 1014 Consumption.py
# Read the distance traveled (in Km) and the spent fuel total (in liters), calculate the average consumption of a car with 12 Km/L.
# Print the result with 3 decimal places after the point.

X = int(input())
Y = float(input())

CONSUMPTION = X / Y

print("%.3f km/l" % CONSUMPTION)

# ]=========================================================================================================================[#

# Path: 1015 Distance Between Two Points.py
# Read the coordinates (x1, y1) and (x2, y2) of two points in the plane, and calculate the distance between them, showing four decimal places after the comma, according to the formula:
# distance = sqrt((x2 - x1)2 + (y2 - y1)2)


x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

DISTANCE = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("%.4f" % DISTANCE)

# ]=========================================================================================================================[#

# Path: 1016 Distance.py
# Read an integer value representing a distance (in Km), calculate how many minutes it takes to walk this distance
# considering that the person walks at 30 Km/h (60 minutes for every 30 Km) and print the result.
# Consider only positive values. Use the input/output format provided in the sample problem.

X = int(input())

TIME = X * 2

print("%d minutos" % TIME)

# ]=========================================================================================================================[#

# Path: 1017 Fuel Spent.py
# Read the time spent in hours and the average speed (12 Km/h) of a car.
# Calculate and print the amount of fuel needed to run the car with the input values.

TIME = int(input())
SPEED = int(input())

FUEL = (TIME * SPEED) / 12

print("%.3f" % FUEL)

# ]=========================================================================================================================[#

# Path: 1018 Banknotes.py
# Read an integer value.
# Calculate the smallest possible number of banknotes in which the value may be decomposed.
# The possible banknotes are 100, 50, 20, 10, 5, 2 and 1.
# Print the read value and the list of banknotes.

N = int(input())

print(N)

print("%d nota(s) de R$ 100,00" % (N / 100))
N = N % 100

print("%d nota(s) de R$ 50,00" % (N / 50))
N = N % 50

print("%d nota(s) de R$ 20,00" % (N / 20))
N = N % 20

print("%d nota(s) de R$ 10,00" % (N / 10))
N = N % 10

print("%d nota(s) de R$ 5,00" % (N / 5))
N = N % 5

print("%d nota(s) de R$ 2,00" % (N / 2))
N = N % 2

print("%d nota(s) de R$ 1,00" % N)

# ]=========================================================================================================================[#

# Path: 1019 Time Conversion.py
# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

SECONDS = int(input())

HOURS = SECONDS / 3600
SECONDS = SECONDS % 3600

MINUTES = SECONDS / 60
SECONDS = SECONDS % 60

print("%d:%d:%d" % (HOURS, MINUTES, SECONDS))

# ]=========================================================================================================================[#

# Path: 1020 Age in Days.py
# Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.
# Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month.

DAYS = int(input())

YEARS = DAYS / 365
DAYS = DAYS % 365

MONTHS = DAYS / 30
DAYS = DAYS % 30

print("%d ano(s)" % YEARS)
print("%d mes(es)" % MONTHS)
print("%d dia(s)" % DAYS)

# ]=========================================================================================================================[#

# Path: 1021 Banknotes and Coins.py
# Read a value of floating point with two decimal places. This represents a monetary value.
# After this, calculate the smallest possible number of banknotes and coins on which the value may be decomposed.
# The possible banknotes are 100, 50, 20, 10, 5, 2.
# The possible coins are 1, 0.50, 0.25, 0.10, 0.05 and 0.01.
# Print the message “NOTAS:” followed by the list of banknotes and the message “MOEDAS:” followed by the list of coins.

VALUE = float(input())

print("NOTAS:")
NOTAS = [100, 50, 20, 10, 5, 2]
for NOTA in NOTAS:
    COUNT = int(VALUE / NOTA)
    print("%d nota(s) de R$ %.2f" % (COUNT, NOTA))
    VALUE -= COUNT * NOTA

print("MOEDAS:")
MOEDAS = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
for MOEDA in MOEDAS:
    COUNT = int(VALUE / MOEDA)
    print("%d moeda(s) de R$ %.2f" % (COUNT, MOEDA))
    VALUE = round(VALUE - COUNT * MOEDA, 2)

# ]=========================================================================================================================[#

# Path: 1035 Selection Test 1.py
# Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

# ]=========================================================================================================================[#

# Path: 1036 Bhaskara's Formula.py
# Read 3 floating point numbers.
# if it is possible to calculates the roots because division by zero or a square root of a negative number, presents the message “Impossivel calcular”.


A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

DELTA = (B ** 2) - (4 * A * C)

if (DELTA < 0) or (A == 0):
    print("Impossivel calcular")
else:
    print("R1 = %.5f" % ((-B + math.sqrt(DELTA)) / (2 * A)))
    print("R2 = %.5f" % ((-B - math.sqrt(DELTA)) / (2 * A)))

# ]=========================================================================================================================[#

# Path: 1037 Interval.py
# Read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100].
# If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo”.

VALUE = float(input())

if (VALUE < 0) or (VALUE > 100):
    print("Fora de intervalo")
elif (VALUE <= 25):
    print("Intervalo [0,25]")
elif (VALUE <= 50):
    print("Intervalo (25,50]")
elif (VALUE <= 75):
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")

# ]=========================================================================================================================[#
