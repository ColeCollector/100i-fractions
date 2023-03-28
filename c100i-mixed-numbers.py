#!python3

# convert mixed numbers to improper fractions
# convert improper fractions to mixed numbers of type a + b/c

def toImproper(a,b,c):
    numer = (a*c) + b
    deno = c

    answer = (numer, deno)
    print(answer)
    return answer

    # a : whole number
    # b : numerator
    # c : denominator


def toMixed(num,den):
    a = num/den
    a = int(a)
    b = num - (a*den)
    c = den
    #num: numerator
    #den: denominator
    # return a: whole number, b: numerator, c: denominator
    answer = (a,b,c)
    print(answer)
    return answer

if __name__ == "__main__":
    assert toMixed(10,3) == (3,1,3)
    assert toMixed(3,4) == (0,3,4)
    assert toMixed(9,2) == (4,1,2)
    assert toImproper(5,1,3) == (16,3)
    assert toImproper(2,1,2) == (5,2)
