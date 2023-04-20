"""
Problem 10.6 [40 points]  Programming Decision Stumps
For this problem you will implement code to compute a "decision stump" (decision tree with just one test at 
the root; see definition in R&N, 4e, p. 700) for a real-life data set.  Here is a linked example decision stump.

The data is a massaged version (to make all variables 0-1 valued and remove instances with missing values) of the 
Congressional Voting Records in the UCI Machine Learning database. There is the classification (Attribute 1; 0=Democrat,
 1=Republican) and 16 attributes (Attributes 2-17), which details votes on various bills taken from the 1984 United States 
 Congressional Voting Records (0=nay, 1=yes).

The massaged data you will use along with a more detailed description appear inside this linked Python notebook 
DecisionStumpBase.ipynb. The program also includes some useful items:

Russell and Norvig's entropy function for boolean variables, B (see p. 662 of R&N, 4e)
Code snippets for summing positive and negative examples of attributes
There is also a C++ version there, but it is not guaranteed and uses different functions as defined in R&N’s Third Edition.

Perform the following
(10 points) Write a subroutine for Remainder(A), described on page 662 of R&N, 4e, that takes as its input value 
for A an integer between 2 and 17 corresponding to Attributes 2-17 as defined in the data file.

(10 points) Write a subroutine for Gain(A), again described on page 662 of R&N, 4e, that again takes an integer input 
as above.

(20 points) Write the necessary code to compute the decision stump. This entails (i) finding the attribute (2-17) that 
maximizes the information gain, (ii) counting how many of each classification appear in each branch, and (iii) computing 
the classifications you should use depending on that attribute's value.  So, you are splitting on the yeses and nays (for 
each vote) and trying to predict the Dems and Reps. IDEA: how can you best predict the rep.’s party by their vote on just 
one particular bill?

We do not want to collect/handle/skim pages of common data and code. Thus, for parts (a) and (b), turn in only the code for 
each subroutine. (By the way, the use of global variables, like table is highly encouraged to ease programming.) For part (c),
 turn in only the code for your new/modified main program. (You may freely use or delete the code in main() of data.cc.)
  
Furthermore, for part (c), record the following in a drawing:
the number of Democrat and Republican classifications in the whole tree,

"""

table=[
    [0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1],
    [1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1],
    [0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,0],
    [0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1],
    [1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1],
    [0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,1],
    [0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1],
    [0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1],
    [0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1],
    [1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1],
    [0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1],
    [0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,1],
    [1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1],
    [0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1],
    [0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1],
    [0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1],
    [0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0],
    [1,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1],
    [0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1],
    [0,1,0,1,0,0,1,1,1,0,1,1,0,1,1,1,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1],
    [1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1],
    [0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1],
    [1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1],
    [1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0],
    [1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1],
    [0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1,1],
    [1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1],
    [1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1],
    [0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0],
    [1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1],
    [0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0],
    [0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1],
    [0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0],
    [0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1],
    [0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0],
    [1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1],
    [0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1],
    [0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1],
    [0,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1],
    [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1],
    [0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1],
    [0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1],
    [0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1],
    [0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1],
    [1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1],
    [0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1],
]




import math
import numpy as np

def B(q):
    if q==0 or q==1:
        return 0
    return -(q*math.log2(q)+(1-q)*math.log2(1-q))

def Remider(A,table):
    pos = 0
    neg = 0
    for col in table:
        if col[A]==1:
            pos+=1
        else:
            neg+=1
    p = pos/(pos+neg)
    n = neg/(pos+neg)
        
    E1 = B(p)
    E2 = B(n)
    Remider = p*E1+n*E2
    return Remider

k = Remider(0,table)
print(k)

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
    E1 = B(p)
    E2 = B(n)
    Gain = entropy - (p*E1+n*E2)
    return Gain

def DecisionTrump(table):
    for i in range(17):
        print(f"Atribut {i} Gain {Gain(i,table)}")

"""
Write the necessary code to compute the decision stump. This entails 
(i) finding the attribute (2-17) 
that maximizes the information gain, 
(ii) counting how many of each classification appear in each branch, 
and 
(iii) computing the classifications you should use depending on that attribute's value.  So, you are 
splitting on the yeses and nays (for each vote) and trying to predict the Dems and Reps. IDEA: how can you 
best predict the rep.’s party by their vote on just one particular bill?
"""

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

    
DecisionStump(table)




"""
1. 
# 5. Number of Instances: 435 (267 democrats, 168 republicans)
#
# MSB NOTE: Any voting record (instance) that contained >=1 unknowns was removed.
# MSB NOTE: This left only 232 of the original 435 instances.
# 6. Number of Attributes: 16 + class name = 17 (all Boolean valued)
#
# MSB NOTE: All attribute values were changed to 0s and 1s as noted below
#
# 7. Attribute Information:
#   1. Class Name: 2 (0=democrat, 1=republican)
#   2. handicapped-infants: 2 (1=y,0=n)
#   3. water-project-cost-sharing: 2 (1=y,0=n)
#   4. adoption-of-the-budget-resolution: 2 (1=y,0=n)
#   5. physician-fee-freeze: 2 (1=y,0=n)
#   6. el-salvador-aid: 2 (1=y,0=n)
#   7. religious-groups-in-schools: 2 (1=y,0=n)
#   8. anti-satellite-test-ban: 2 (1=y,0=n)
#   9. aid-to-nicaraguan-contras: 2 (1=y,0=n)
#  10. mx-missile: 2 (1=y,0=n)
#  11. immigration: 2 (1=y,0=n)
#  12. synfuels-corporation-cutback: 2 (1=y,0=n)
#  13. education-spending: 2 (1=y,0=n)
#  14. superfund-right-to-sue: 2 (1=y,0=n)
#  15. crime: 2 (1=y,0=n)
#  16. duty-free-exports: 2 (1=y,0=n)
#  17. export-administration-act-south-africa: 2 (1=y,0=n)
"""
