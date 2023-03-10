#!python3

# program to add 2 fractions
# return the sum of the 2 fractions as a tuple with numerator and
# denominator in lowest terms
def sum(n1,d1,n2,d2):

    n1 = n1 *d2
    n2 = n1 *d1

    d1 = d1*d2
    d2 = d1*d2

    numerator = n1+n2
    denominator = d1

    for i in range(1,60):
        if numerator%i == 0 and denominator%i == 0:
            numerator = numerator/i
            denominator = denominator/i

    answer = (n1,d1,n2,d2)
    return answer


if __name__ == "__main__":
    assert sum(1,3,2,1) == (7,3)
    assert sum(1,4,3,4) == (1,1)
    assert sum(5,2,3,5) == (31,10)
