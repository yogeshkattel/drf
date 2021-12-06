def _fib(n):
    if n < 2:
        return 1
    else:
        return _fib(n-1) + _fib(n-2)

print(_fib(1))