#!python3

# program to add 2 fractions
# return the sum of the 2 fractions as a tuple with numerator and
# denominator in lowest terms
def sum(n1,d1,n2,d2):

    numer1 = n1*d2
    numer2 = n2*d1

    denom1 = d1*d2
    denom2 = d1*d2

    numerator = numer1+numer2
    denominator = denom1

    for i in range(1,20):
        if numerator%i == 0 and denominator%i == 0:
            numer = numerator/i
            denom = denominator/i

    answer = (numer, denom)
    print(answer)
    return answer


if __name__ == "__main__":
    assert sum(1,3,2,1) == (7,3)
    assert sum(1,4,3,4) == (1,1)
    assert sum(5,2,3,5) == (31,10)
