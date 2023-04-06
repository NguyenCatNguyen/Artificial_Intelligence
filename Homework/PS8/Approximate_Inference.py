from random import random

TRIALS = 10**6

evidence = 0
query = 0
pall = []
pdenomall = []
joint_observed = 0
pjointall = []

for trial in range(1,TRIALS+1):
    randB, randE = random(), random()
    B = randB < 0.001
    E = randE < 0.002
    if B and E:
        randA = random()
        A = randA < 0.98
    elif B and not E:
        randA = random()
        A = randA < 0.95
    elif not B and E:
        randA = random()
        A = randA < 0.29
    else:
        randA = random()
        A = randA < 0.001
    randJ, randM = random(), random()
    if A:
        J = randJ < 0.95
        M = randM < 0.7
    else:
        J = randJ < 0.01
        M = randM < 0.01
    # DIRECT SAMPLING FOR JOINT PROB. ESTIMATE
    if (not J) and (not M) and B and E:
        joint_observed += 1
        pjointall.append(joint_observed/trial)
    # REJECTION SAMPLING: ONLY PROCESS IF EVIDENCE True
    if not M:
        evidence += 1
        if not J:
            query += 1
        p = query/evidence
        pall.append(p)
    pdenom = evidence/trial
    pdenomall.append(pdenom)

print("P(!J,!M,B,E) ~=", pjointall[-1])
