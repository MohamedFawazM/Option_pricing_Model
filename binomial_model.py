import numpy as np

def binomial_price(S, K, T, r, sigma, option_type="call", steps=100):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    prices = np.zeros((steps + 1, steps + 1))
    for i in range(steps + 1):
        for j in range(i + 1):
            prices[j, i] = S * (u ** (i - j)) * (d ** j)

    option = np.zeros_like(prices)
    for j in range(steps + 1):
        option[j, steps] = max(0, prices[j, steps] - K) if option_type == "call" else max(0, K - prices[j, steps])

    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            option[j, i] = np.exp(-r * dt) * (q * option[j, i + 1] + (1 - q) * option[j + 1, i + 1])

    return option[0, 0]
