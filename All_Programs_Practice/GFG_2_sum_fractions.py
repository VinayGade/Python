
def sum(num1, den1, num2, den2):
    num3=1
    den3=1
    if den1 == den2:
        den3=den2
        num3=num1+num2
    elif den1%den2 == 0:
        den3=den1
        num2=num2*den1/den2
        num3=num1+num2

    elif den2%den1 == 0:
        den3 = den2
        num1 = num1 * den2 / den1
        num3 = num2 + num1

    return num3+"/"+den3


T = int(input())
for x in range(0,T):
    num1 = int(input())
    den1 = int(input())
    num2 = int(input())
    den2 = int(input())
    print(sum(num1, den1, num2, den2))