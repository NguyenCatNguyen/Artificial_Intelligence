def run_simulation(start_location, environment, table):
    # initialize the performance score
    score = 0
    # initialize the current location
    current_location = start_location
    # initialize the current state
    current_state = environment
    
    # loop until all rooms are clean
    while any(value == 'Dirty' for value in current_state.values()):
        # check if the current room is dirty
        if current_state[current_location] == 'Dirty':
            # clean the room
            current_state[current_location] = 'Clean'
            # increment the performance score
            score += 1
            # get the next action from the table
            next_action = table[(current_location, 'Clean')]
        else:
            # get the next action from the table
            next_action = table[(current_location, 'Clean')]
        
        # check if the next action is to move left
        if next_action == 'Left':
            current_location = 'A' if current_location == 'B' else 'B'
        # check if the next action is to move right
        elif next_action == 'Right':
            current_location = 'B' if current_location == 'A' else 'A'
    
    # print the environment, start location, and performance score
    print('Environment:', environment)
    print('Start Location:', start_location)
    print('Performance Score:', score)

# define the environment
environment = {'A': 'Dirty', 'B': 'Dirty'}
# define the start location
start_location = 'A'

# define the locations
loc_A = 'A'
loc_B = 'B'


# define the stimulus-response table
table = {((loc_A, 'Clean'),): 'Right',
         ((loc_A, 'Dirty'),): 'Suck',
         ((loc_B, 'Clean'),): 'Left',
         ((loc_B, 'Dirty'),): 'Suck',
         ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
         ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
         ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
         ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
         ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
         ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'}

# run the simulation
run_simulation(start_location, environment, table)
