import random
import matplotlib.pyplot as plt

def simulate_coin_flip(prob_heads, num_tosses):
    num_heads = 0
    for _ in range(num_tosses):
        if random.random() < prob_heads:
            num_heads += 1
    return num_heads

prob_heads = 0.3
n_values = list(range(1, 100001))
num_heads_list = [simulate_coin_flip(prob_heads, n) for n in n_values]

plt.plot(n_values, num_heads_list)
plt.axhline(y=prob_heads * 100000, color='r', linestyle='--', label='Expected Heads')
plt.xlabel('Number of Tosses')
plt.ylabel('Number of Heads')
plt.legend()
plt.title('Simulating Coin Flips with Probability of Heads = 0.3')
plt.show()
