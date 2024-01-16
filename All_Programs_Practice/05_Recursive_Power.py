def power(x, n):
    if n == 0:
        return 1;
    elif n == -1:
        return 1/x;
    elif n < 0:
        return 1 /  power(x, -n);
    else :
        return x*power(x,n-1);

print(power(2,4));
print(power(10,-1));
print(power(3,3));
print(power(10,2));
print(power(100,-2));
