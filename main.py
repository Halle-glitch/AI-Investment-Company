from agents.fundamental import FundamentalAnalyst
from agents.seasonality import SeasonalityAnalyst


print("AI Investment Company")


# Seasonality analysis
analyst = SeasonalityAnalyst()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# Analyse all months
results = []

for month in months:
    result = analyst.analyse("Company A", month)
    results.append(result)


# Calculate the seasonality scores
results = analyst.calculate_scores(results)

print(results)