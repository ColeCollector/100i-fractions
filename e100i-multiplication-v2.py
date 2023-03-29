#!python3

# Duplicate of d100i-multiplication.py
# except this should accept mixed numbers:

def product(f1,f2):
    # f1: tuple representing first fraction
        # a tuple with length 2 is a numerator/denominator 
        # a tuple with length 3 is a whole number/numerator/denominator
    # f2 is the same as 1
    
    if len(f1) == 2:
        numer = f1[0]
        deno = f1[1]   

    if len(f1) == 3:
        whole = f1[0]
        n1 = f1[1]
        d1 = f1[2]

        numer = (whole*d1) + n1
        deno = d1

    if len(f2) == 2:
        numer2 = f2[0]
        deno2 = f2[1]
    
    if len(f2) == 3:
        whole2 = f2[0]
        n2 = f2[1]
        d2 = f2[2]

        numer2 = (whole2*d2) + n2
        deno2 = d2

    finaldeno = deno*deno2
    finalnumer = numer*numer2
    answer = (finalnumer,finaldeno)
    print(answer)
    return answer

if __name__ == "__main__":
    assert product((1,3),(4,1,2)) == (9,6)
    assert product( (3,4) , (5,3) ) == (15,12)
    assert product( (3,1,2) , (2,1,2) ) == (35,4)