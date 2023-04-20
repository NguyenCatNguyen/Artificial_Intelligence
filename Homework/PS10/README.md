# PS10

- `Entropy` 

## Problem 10.2
a. What is the entropy of this set of training examples with respect to the target function classification?



```python

import math
import numpy as np
# Define Entropy
def B(q):
    if q==0 or q==1:
        return 0
    return -(q*math.log2(q)+(1-q)*math.log2(1-q))
```
## Part A
```python
def Remider(A,table):
    pos = 0
    neg = 0
    for col in table: # table contains the data, in each col there are 17 values
        if col[A]==1:
            pos+=1
        else:
            neg+=1
    p = pos/(pos+neg)
    n = neg/(pos+neg)
        
    E1 = B(p) # child 1
    E2 = B(n) # child 2
    Remider = p*E1+n*E2 
    return Remider
```
## Part B
```python
def Gain(A,table):
    pos = 0
    neg = 0
    for col in table:
        if col[A]==1:
            pos+=1
        else:
            neg+=1
    p = pos/(pos+neg)
    n = neg/(pos+neg)
    entropy = B(p/(p+n))    
    E1 = B(p) # child 1
    E2 = B(n) # child 2
    Gain = entropy - (p*E1+n*E2)
    return Gain
```

## Part C
```python
def DecisionStump(table):
    Atri = []
    # Keep track of the number of Dems and Reps
    Dem = 0
    Rep = 0
    for col in table:
        if col[0] ==1:
            Dem +=1
        else:
            Rep +=1
    # Find the attribute that maximizes the information gain
    for i in range(17):
        Atri.append(Gain(i,table))
    Atri = np.array(Atri)
    Atri = np.argsort(Atri)
    Atri = Atri[::-1]
    # Count how many of each classification appear in each branch
    for i in range(17):
        pos = 0
        neg = 0
        for col in table:
            if col[Atri[i]]==1:
                pos+=1
            else:
                neg+=1
        p = pos/(pos+neg)
        n = neg/(pos+neg)
        print(f"Attribute {Atri[i]} has {p} positive and {n} negative")
    # Compute the classifications you should use depending on that attribute's value    
    for i in range(17):
        pos = 0
        neg = 0
        for col in table:
            if col[Atri[i]]==1:
                pos+=1
            else:
                neg+=1
        p = pos/(pos+neg)
        n = neg/(pos+neg)
        if p > n:
            print(f"Attribute {Atri[i]} has {p} positive and {n} negative, so we predict positive")
        else:
            print(f"Attribute {Atri[i]} has {p} positive and {n} negative, so we predict negative")
    return Atri

```