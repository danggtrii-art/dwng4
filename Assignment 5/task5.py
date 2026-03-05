import random
N = int(input("Enter number of random points: "))
inside = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside += 1
pi_value = 4 * inside / N
print("Approximate value of pi:", pi_value)