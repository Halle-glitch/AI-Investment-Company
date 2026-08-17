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

best_month = analyst.find_best_month(results)
worst_month = analyst.find_worst_month(results)

print("Best month:", best_month["month"])
print("Worst month:", worst_month["month"])

print(results)