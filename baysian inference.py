import numpy as np
import matplotlib.pyplot as plt

# Simulate coin flips
np.random.seed(42)
flips = np.random.choice(['H', 'T'], size=100, p=[0.7, 0.3])

# Count heads and tails
heads = np.sum(flips == 'H')
tails = np.sum(flips == 'T')

# Define the prior distribution (uniform)
theta_values = np.linspace(0, 1, 100)
prior = np.ones_like(theta_values)

# Define the likelihood
likelihood = theta_values**heads * (1 - theta_values)**tails

# Compute the posterior distribution
posterior = likelihood * prior
posterior /= posterior.sum()

# Plot the prior, likelihood, and posterior distributions
plt.figure(figsize=(12, 6))
plt.plot(theta_values, prior, label='Prior', linestyle='--')
plt.plot(theta_values, likelihood, label='Likelihood', linestyle='--')
plt.plot(theta_values, posterior, label='Posterior', linewidth=2)
plt.xlabel('Theta')
plt.ylabel('Probability')
plt.title('Bayesian Inference: Prior, Likelihood, and Posterior')
plt.legend()
plt.show()
