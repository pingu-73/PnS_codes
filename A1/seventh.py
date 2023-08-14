import random
import matplotlib.pyplot as plt

def estimate_pi(n):
    points_inside_circle = 0
    for _ in range(n):
        x = random.random()  
        y = random.random()  
        distance = x**2 + y**2 

        if distance <= 1:
            points_inside_circle += 1

    estimated_pi = (points_inside_circle / n) * 4
    return estimated_pi

n_values = list(range(1, 100001))
pi_estimates = [estimate_pi(n) for n in n_values]

plt.plot(n_values, pi_estimates)
plt.axhline(y=3.141592653589793, color='r', linestyle='--', label='True π')
plt.xlabel('Number of Simulated Points')
plt.ylabel('Estimated π Value')
plt.legend()
plt.title('Estimating π using Monte Carlo Method')
plt.show()
