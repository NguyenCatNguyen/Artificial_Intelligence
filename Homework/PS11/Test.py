import numpy as np

# Define the data set and desired outputs
I = np.array([[1, 0, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1], [0, 0, 1], [1, 0, 1]])
O = np.array([1, 0, 1, 0, 0, 1])

# Initialize the weight vector with zeros
w = np.zeros(I.shape[1] + 1) # Bias weight 

# Set the learning rate and maximum number of epochs
alpha = 1
max_epochs = 100

# Train the perceptron using the Perceptron Learning Rule
for epoch in range(max_epochs):
    weights_changed = False
    for i in range(I.shape[0]):
        net_input = np.dot(w[1:], I[i]) + w[0]  # add bias weight
        net_output = 1 if net_input > 0 else 0
        if net_output != O[i]:
            w[1:] += alpha * (O[i] - net_output) * I[i]
            w[0] += alpha * (O[i] - net_output)  # update bias weight
            weights_changed = True
    if not weights_changed:
        print("Converged after {} epochs".format(epoch + 1))
        break
    print(f"{net_input} -> {net_output}")

# Print the final weight vector
print("Final weight vector: ", w)
