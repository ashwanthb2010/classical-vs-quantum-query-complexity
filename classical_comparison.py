# Example function
# Returns 0 for even numbers and 1 for odd numbers
def f(x):
    return x % 2

# Function to check whether f(x) is constant or balanced
def is_constant(n):

    # Store the output of the first input
    first = f(0)

    # Check all remaining inputs
    # Total possible inputs = 2^n
    for i in range(1, 2**n):

        # Compare current output with first output
        if f(i) != first:

            # If any output differs, function is balanced
            return "Balanced"

    # If all outputs are same, function is constant
    return "Constant"

# Run the function for n = 3
print(is_constant(3))