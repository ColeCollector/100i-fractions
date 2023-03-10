#!python3

# Create a function that receives 2 parameters:
# numerator (integer) and denominator (integer)
# return a tuple of 2 integers (numerator, denominator) for 
# the fraction in lowest terms

def lowestTerms(numerator,denominator):
    print(numerator)
    print(denominator)

    for i in range(1,60):
        if numerator%i == 0 and denominator%i == 0:
            numerator = numerator/i
            denominator = denominator/i
            

    answer = (numerator, denominator)
    print(answer)
    return answer



def main():
    assert lowestTerms(2,4) == (1,2)
    assert lowestTerms(32,40) == (4,5)
    assert lowestTerms(29,87) == (1,3)
    assert lowestTerms(250,400) == (5,8)


if __name__ == "__main__":
    main()

    