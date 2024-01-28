import json
import numpy as np

# Load threshold data
with open('threshold_data.json', 'r') as f:
    threshold_data = json.load(f)

thresholds = threshold_data['thresholds']
count_below_threshold_range = threshold_data['count_below_threshold']
average_below_threshold_range = threshold_data['average_below_threshold']



# Convert numpy int64 types to int for JSON serialization
# Constants
ELECTROLYZER_EFFICIENCY = 50  # kWh per kg
CAPEX = 1000000  # Rupees per kg per hour
WATER_USAGE = 12.5  # liters per kg
SELLING_PRICE = 300  # Rupees per kg
DISTILLED_WATER_RATE = 8
SUBSIDY_PER_KG = 30

# Keep capacity constant at 1 kg per hour
CAPACITY = 1

# Results list
results = []


for i, threshold in enumerate(thresholds):
    ELECTRICITY_RATE = average_below_threshold_range[i] / 1000  # Convert to Rupees per kWh
    num_hours_per_year = (count_below_threshold_range[i] / 4)  # Calculate number of hours per year

    # Input cost calculation
    input_cost = (ELECTRICITY_RATE * ELECTROLYZER_EFFICIENCY) + (WATER_USAGE * DISTILLED_WATER_RATE)

    # Profit per kg calculation
    profit_per_kg = SELLING_PRICE - input_cost + SUBSIDY_PER_KG

    # Profit per hour calculation
    profit_per_hour = profit_per_kg * CAPACITY

    # Profit per year calculation
    profit_per_year = profit_per_hour * num_hours_per_year

    # IRR calculation
    IRR = profit_per_year / (CAPEX / 5)  # Amortized over 5 years

    results.append({
        "threshold_price": threshold,
        "average_electricity_rate": ELECTRICITY_RATE,
        "count_below_threshold": count_below_threshold_range[i],
        "num_hours_per_year": num_hours_per_year,
        "profit_per_year": profit_per_year,
        "IRR": IRR
    })

for result in results:
    result["threshold_price"] = int(result["threshold_price"])
    result["count_below_threshold"] = int(result["count_below_threshold"])
    result["num_hours_per_year"] = int(result["num_hours_per_year"])
    result["profit_per_year"] = float(result["profit_per_year"])
    result["IRR"] = float(result["IRR"])

# Save the corrected results to a JSON file
with open('./profit_calculator_results_with_subsidy.json', 'w') as f:
    json.dump(results, f)