# Artificial Intelligence: A Modern Approach

## Index

### Chapter 1 Introduction
#### 1.1 What is AI?
- `Artificial Intelligence` is the science and engineering of making intelligent machines.
- **Turing Test**
    - A computer is said to pass the Turing Test if a human interrogator cannot distinguish between the computer's output and that of a human.
    - Turning test proposed by Alan Turning in 1950.
    - Design which the question "Can machines think?".
    - The test is not a test of intelligence, but rather a test of a machine's ability to simulate intelligence.
    - The computer would need the following capabilities:
        - `Natural language processing` to communicate successfully in a human language.
        - `Knowledge representation` to store and manipulate knowledge.
        - `Automated reasoning` to answer questions and draw new conclusions.
        - `Machine learning` to adapt to new circumstances and to detect and extrapolate patterns.

## Chapter 2 Intelligent Agent
### 2.1 Agents and Enviroments
- An *agent* is anything that can be viewed as perceiving its *enviroment* through *sensors* and acting upon that enviroment through its *actuators*.
    - Environment: everything outside the agent.
    - Sensors: input from the environment.
    - Actuators: output to the environment.







    
### 2.3 The Nature of Enviroment
- `Task Enviroments` is 
- `PEAS` is a description of the task enviroment
    - Performance Measure is the goal of the agent
    - Environment is the enviroment that the agent is in.
    - Actuators is the action that the agent can do.
    - Sensors is the input that the agent can get.

### Chapter 3 Solving Problems By Searching
```
In which we see how an agent can look ahead to find a sequence of actions that will eventually achieve its goal.
```
- When the correct action to take is not immediately obvious, an agent may need to plan ahead; to cosider a *sequence* of actions that form a path to a goal state. Such an agent is called a ` problem-solving agent`
#### 3.1 Problem-Solving Agents
- When an agent has no information - the enviroment is unknow, the agent can do no better than to execute one of the actions at random

-`Goal formulation`: The agent adopts the *goal* of reaching Bucharest. Goals organize behavior by limiting the objectives and hence the actions to be considered. 
- `Problem formulation`: The agent devises a descripti
### 3.3 Search Algorithms
#### 3.3.1 Best-First Search
- `Best-First Search` is a general-purpose algorithm for finding a path through a graph to a goal node.



## Chapter 4 Search in Complex Enviroments
### 4.1 Local Search and Optimization Problems.
- `Local search` algorithms operate by searching from a start state to neighboring states, without keeping track of the paths, nor the set of states that have been reached. 
    - CONS:
        - They are not systematic(có hệ thống). 
        - They might never explore a portion of the search space where a solution are resside.
    - PROS: however, they have two advantages.
        - They use less memory than other algorithms.
        - They can often find reasonable solutions in large or infinite state spaces for which systematic algorithms are unsuitable.
- `Optimization problems` are problems in which the goal is to find the best solution from a set of possible solutions.

