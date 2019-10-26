num = int(input("Enter the number: "))
def factorial(n):
    a = 1
    while n >= 1:
        a = a * n
        n = n - 1
    return a

q = factorial(num)
print(q)
range