# code
def _is_perfect_(number):
    sum = 1
    if _is_prime_(number):
        return 0;
    else:
        for i in range(2, int(number / 2)+1):
            if number % i == 0:
                sum = sum + i

        if sum == number:
            return 1;
        else:
            return 0;


def _is_prime_(number):
    flag = True
    for i in range(2, int(number / 2)+1):
        if number % i == 0:
            flag = False
            break

    return flag;


def _is_perfect_1(number):
    sum = 1
    temp = number
    x = 0
    maximum = 1
    while temp % 2 == 0:
        x = x+1
        maximum = int(pow(2,x))
        sum = sum + maximum
        temp = temp / 2

    sum = sum+temp
        #while n % 2 == 0:
            #number = number / 2
    for i in range(maximum+1, int(number / 2),2):
        if number%i == 0:
            sum = sum + i
                #number = number / i

    if sum == number:
        return 1;
    else:
        return 0;


T = int(input())
for x in range(0,T):
    N = int(input())
    print(_is_perfect_1(N))
#print(_is_perfect_(6))





