uservalue = int(input("Enter a decimal number: "))
a = 0
b = 1
while uservalue> 0:
        a= a +(uservalue % 2)* b
        uservalue=uservalue// 2
        b=b*10
print(a)