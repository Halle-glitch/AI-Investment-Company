from agents.seasonality import SeasonalityAnalyst


print("AI Investment Company")


# Seasonality analysis
analyst = SeasonalityAnalyst()


# Analyse both companies
analysis_A = analyst.analyse_company("Company A")
analysis_B = analyst.analyse_company("Company B")


analyses = [analysis_A, analysis_B]

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