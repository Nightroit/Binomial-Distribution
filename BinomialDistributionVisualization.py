import matplotlib.pyplot as plt

# Function to calculate factorial.
def factorial(x):
    result = 1
    while x:
        result *= x
        x -= 1
    return result

# Function to calculate combinatorics.
def ncr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

# y-coordinates values.
x = []
for i in range(13):
    x.append(i)

# Calculating y-values and generating co-ordinates.
y = []
probability = 0
for i in range(13):
    output = ncr(20, i)*((0.41)**i)*((0.59)**(20-i))
    y.append(output)
    probability += output

# Plotting output through matplotlib
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title('Simple 2D Plot')
plt.show()

print(probability)
