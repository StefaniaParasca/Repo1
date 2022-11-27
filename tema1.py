#1. if else este o conditionare data unei valori
# 2.
x = 8
if x % 4 >= 0:
    print("numar natural")
else:
    print("nu e numar natural")
# 3.
if x > 0:
    print("numar pozitiv")
elif x == 0:
    print("numar neutru")
else:
    print("numar negativ")
# 4.
if x >= -2 or x <= 12:
    print("numarul e intre valori")
else:
    print("nu este intre valori")
# 5.
y = 10
if x - y < 5:
    print("este mai mica de 5")
else:
    print("este mai mare de 5")
# 6.
print(not (x > 5 or x < 27))
# 7
x = 5
y = 7
print(x == y)
print(x < y)
# 8.
x = 90
y = 60
z = 30
if x == 90:
    print("triunghi dreptunghic")
elif x == 30 or y == 30:
    print("triunghi echilateral")
else:
    print("triunghi oarecare")
# 9
x = "A"
if x == ("A" or "E" or "I" or "O" or "U"):
    print("este vocala")
else:
    print("este consoana")
# 10
x = 3
if x >= 9:
    print("A")
elif x >= 8:
    print("B")
elif x >= 7:
    print("C")
elif x >= 6:
    print("D")
elif x >= 4:
    print("E")
else:
    print("F")