import streamlit as st

st.set_page_config(page_title="Option Pricing (India)", layout="centered")

from datetime import date
from bs_model import black_scholes
from monte_carlo import monte_carlo_price
from binomial_model import binomial_price

st.title(" Indian Option Pricing ")

S = st.number_input("Spot Price (S)", value=23000.0)
K = st.number_input("Strike Price (K)", value=23200.0)
expiry = st.date_input("Expiry Date", value=date(2025, 6, 27))
today = date.today()
T = max((expiry - today).days / 365.0, 0.0001)
r = st.number_input("Risk-Free Rate (r)", value=0.065, format="%.4f")
sigma = st.number_input("Volatility (σ)", value=0.20, format="%.2f")
option_type = st.selectbox("Option Type", ["call", "put"])
model = st.selectbox("Pricing Model", ["Black-Scholes", "Monte Carlo", "Binomial Tree"])

if st.button("Calculate Option Price"):
    if model == "Black-Scholes":
        price = black_scholes(S, K, T, r, sigma, option_type)
    elif model == "Monte Carlo":
        price = monte_carlo_price(S, K, T, r, sigma, option_type)
    else:
        price = binomial_price(S, K, T, r, sigma, option_type)

    st.success(f"{option_type.capitalize()} option price using {model}: ₹{price:.2f}")
