import numpy as np

def monte_carlo_price(S, K, T, r, sigma, option_type="call", n_sim=10000):
    Z = np.random.normal(0, 1, n_sim)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0) if option_type == "call" else np.maximum(K - ST, 0)
    return np.exp(-r * T) * np.mean(payoff)
