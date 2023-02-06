# Artificial_Intelligence
 The purpose of this repo is for daily note about AI Lessons

## Index



## Lecture 3: Rational Agents
- `Rational Agent` - "Do the right thing"
- `Agent` is anything that can be viewed as perceiving 
its enviroment through sensors and acting upon that
evinroment through *actuators*.
- `Rational` (correct agent function) depends on
    - 1. Performance Measure (win as chess)
    - 2. Prior Knowledge (rule)
    - 3. Actions(s) available (move)
    - 4. Percept history to date (all the move in the game so far)
    - 5. Memory and physical limitations
    Rational Agent maximize it performance measure and subject to its ability and limitations.
- `Task Environment`
    - Performance Measure
    - Environment
    - Actuators
    - Sensors

- Rational Agent Architecture:
    - Environment(plan) -> Agent  (percept)
    - Agent -> Action
    - Agent -> State
    - Agent -> Performance Measure
### Example: Photovore Robot
- Percepts at time t, [0] or [1] no light or light 
- Actuator at [0] or [1] stay or move
- If light, stay, else move

=> This type of robot  is call  `Stimulus response agent`.
- Condition/action rule
### Different between Percept Space and Percept History.
1. Percept, Binary value time T, 2 posible value.
- Percept History

### Spectrum of Agent 
- Agent can be thought throw two axit
    - Reflexive => Deliberative
    - Tactical => Strategic
- What make action (the )

### Stig mergy 
- Been use by bees, termite, and ants to find food.
- Puck-Pilling robot
    - Rule that they use for this robot:
        - Go straight => Turn at random
- Stigmergy def: work from the product of work. 
- Complexity of behavior due to complexity of environment.
- Table setting at a royal wedding
- QUESTION: How much of your intelligience is due to your environment? Is it due to your environment or your genes?

### Configuration space of agent/system


## Lecture 4: Intelligent Agent
- `Intelligent Agent` - "Do the right thing"




## Lecture: 
- `A*` is complete and optimal
    - if heristic is admissible 
        - h(n) <= h*(n)
    - if heristic is consistent
        - h(n) <= c(n, n') + h(n')
        - if n' is reachable from n
### Note  
- Why not use `h*`?
    - `h*` is not always known
    - `h*` is not always computable
    -  Too Expensive to compute
- So in general, we want the most informative heuristic that we have time to compute.
- Limited search to obtain better heuristic



### 2.1 Agents and Enviroments
- An **agent** is anything that can be viewed as perceiving its **enviroment** through **sensors** and acting upon that enviroment through its **actuators**.
    - Environment: everything outside the agent.
    - Sensors: input from the environment.
    - Actuators: output to the environment.
- `Percept` the content an agent's sensors are perceiving.
- An agent's **percet sequence** is the complete history of all percepts it has ever received.
```
- An agent's choice of action at any given instant can depend on its built-in knowledge and on the entire percept seqquence observed to date.
```
- An agent's behavior is described by the `agent function` that maps any given percept sequence to an action.

![Agent](Graphs/Agents_interact.png)
- `Tabulating` the agent function that describes any given agent's.
- The agent function for an atificial agent will be implemented by an **agent program**.
- To illustrate these ideas, we have a simple example of a vacuum cleaner agent.

![Vacuum](Graphs/The_Vaccuum.png)
### 2.2 Good Behavior: The Concept of Rationality
- A `ration agent` is one that does the right thing.
 
 #### Performance Measure
    - A `performance measure` is a numerical function of the agent's performance.
    - AI is generally stuck to one notion called `consequentialism` which is the idea that the right thing to do is the thing that produces the best consequences.