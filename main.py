def create_fibo():
    fibo = [0, 1]
    for i in range(2, int(input(">Select Fibonacci sequence depth.. "))):
        fibo.append(fibo[i-2] + fibo[i-1])
    return fibo


def is_fibo(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return is_fibo(arr, low, mid - 1, x)
        else:
            return is_fibo(arr, mid + 1, high, x)
    else:
        return False


fibo_list = create_fibo()
print(is_fibo(fibo_list, 0, len(fibo_list), int(input(">Value to search for: "))))
