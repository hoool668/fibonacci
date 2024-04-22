def fibonacci(n):
    # 初始化前两个斐波那契数
    fib = [0, 1]

    # 生成斐波那契数列
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib

# 生成前 10 个斐波那契数
fibonacci_sequence = fibonacci(10)

# 打印结果
print(fibonacci_sequence)
