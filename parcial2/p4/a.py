def f_recur(n: int) -> int:
    if 0 <= n < 36:
        return n
    else:
        return sum([f(n - 6* i) for i in range(1, 6)])