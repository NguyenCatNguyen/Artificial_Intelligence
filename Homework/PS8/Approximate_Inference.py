from random import random

TRIALS = 10**6
A = 1/2  # prior probability of A

evidence = 0
query = 0
pdenomall = []
pdnumall = []

for trial in range(1, TRIALS + 1):
    randA, randB, randC = random(), random(), random()
    A_val = randA < A  # sample A
    B_val = randB < (1 if A_val else 1/2)  # sample B
    C_val = randC < (1 if A_val else 1/2)  # sample C
    D_val = B_val and C_val  # sample D
    
    # compute denominator P(D)
    pdenom = (1 if A_val else 1/2) * (1 if B_val else 1/2) * (1 if C_val else 1/2)
    pdenomall.append(pdenom)
    
    # compute numerator P(D|A) * P(A)
    if A_val == True and D_val == True:
        pdnum = 1 * A_val
        pdnumall.append(pdnum)
    
    # increment evidence counter if D is observed
    if D_val == True:
        evidence += 1
        # increment query counter if A is not true
        if A_val == False:
            query += 1
    
print("P(A|D) ~=", sum(pdnumall)/sum(pdenomall))
