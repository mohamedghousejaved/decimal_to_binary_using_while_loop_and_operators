a = int(input("Enter a decimal number: "))
b = 0
c = 1
while a > 0:
        b = b +(a % 2)* c
        a =a// 2
        c =c*10
print(b)