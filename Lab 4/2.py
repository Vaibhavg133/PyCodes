def fibonacci(n):
    p = 0
    print p
    c = 1
    print c
    for i in range(n):
        total = p + c
        print total
        p = c
        c = total
