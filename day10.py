import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Central Tendency
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)[0]

# Dispersion
range_ = np.ptp(data)
variance = np.var(data)
std_dev = np.std(data)

print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Range: {range_}, Variance: {variance}, Standard Deviation: {std_dev}")



