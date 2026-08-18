from agents.seasonality import SeasonalityAnalyst


print("AI Investment Company")


# Seasonality analysis
analyst = SeasonalityAnalyst()

analysis = analyst.analyse_company("Company A")

results = analysis["results"]
best_month = analysis["best_month"]
worst_month = analysis["worst_month"]

print("Best month:", best_month["month"])
print("Worst month:", worst_month["month"])

for result in results:
    print(
        result["month"],
        "Average:", round(result["average_return"], 2),
        "Consistency:", round(result["consistency_score"], 2),
        "Stability:", round(result["stability_score"], 2),
        "Score:", round(result["seasonality_score"], 2)
    )

print("Best month:", best_month["month"])
print("Best score:", round(best_month["seasonality_score"], 2))

print("Worst month:", worst_month["month"])
print("Worst score:", round(worst_month["seasonality_score"], 2))