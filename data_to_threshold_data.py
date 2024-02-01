import numpy as np
import json

with open('./data.json') as f:
    data = json.load(f)

updated_prices = []
for date, time_data in data.items():
    for entry in time_data:
        updated_prices.append(int(entry[2]))


# Define threshold values in intervals of 50
thresholds = np.arange(min(updated_prices), max(updated_prices) + 50, 50)
count_below_threshold = [len([price for price in updated_prices if price < threshold]) for threshold in thresholds]
average_below_threshold = [np.mean([price for price in updated_prices if price < threshold]) if count_below_threshold[i] > 0 else 0 for i, threshold in enumerate(thresholds)]

threshold_data = {
    "thresholds": thresholds.tolist(),
    "count_below_threshold": count_below_threshold,
    "average_below_threshold": average_below_threshold
}

with open('threshold_data.json', 'w') as f:
    json.dump(threshold_data, f)