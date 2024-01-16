
def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1;
    else:
        result = n;
        i = n;
        while i >= 2:
            i = i-1;
            result = result * i;
    # Implement this function

    return result;


print(factorial(5));