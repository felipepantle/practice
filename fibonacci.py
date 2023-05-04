def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print("demo fibonacci numbers")
i = 0 
while i < 20:
    print(fib(i))
    i += 1

print("finished")

def interactive_mode():
    n = int(input("Enter how many fibonacci numbers you want to see: "))
    i = 0 
    while i < n:
        print(fib(i))
        i += 1



interactive_mode()


