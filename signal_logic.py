import random

def check_signals():
    dummy_signals = [
        "Buy signal: BTCUSDT at $30,200",
        "Buy signal: ETHUSDT at $1,900",
    ]
    return [random.choice(dummy_signals)] if random.random() > 0.6 else []