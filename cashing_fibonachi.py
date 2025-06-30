def caching_fibonacci():
    cash = {} 
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cash.keys(): #checking if fibonacchi(n) exist in cash
            return cash[n]
        else:
            cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cash[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(15))