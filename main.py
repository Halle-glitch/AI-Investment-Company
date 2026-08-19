from agents.seasonality import SeasonalityAnalyst


print("AI Investment Company")


# Seasonality analysis
analyst = SeasonalityAnalyst()


companies = [
    "Company A",
    "Company B",
    "Company C",
    "Company D",
    "Company E"
]

analyses = []

for company in companies:
    analysis = analyst.analyse_company(company)
    analyses.append(analysis)


for analysis in analyses:

    company = analysis["company"]
    results = analysis["results"]
    best_month = analysis["best_month"]
    worst_month = analysis["worst_month"]

    print("")
    print(company)
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