from agents.seasonality import SeasonalityAnalyst
from agents.fundamental import FundamentalAnalyst
from agents.decision import DecisionAgent



def print_seasonality_analysis(analysis):

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

print("AI Investment Company")

fundamental_analyst = FundamentalAnalyst()
seasonality_analyst = SeasonalityAnalyst()
decision_agent = DecisionAgent()

companies = [
    "Company A",
    "Company B"
]

analyses = []

for company in companies:

    seasonality_result = seasonality_analyst.analyse_company(company)
    if company == "Company A":
        fundamental_result = fundamental_analyst.analyse("Company A", 15, 20, 20, 10)

    elif company == "Company B":
        fundamental_result = fundamental_analyst.analyse("Company B", -8, 3, 70, -10)

    company_analysis = {
        "company": company,
        "seasonality": seasonality_result,
        "fundamental": fundamental_result
    }

    analyses.append(company_analysis)

for analysis in analyses:

    fundamental = analysis["fundamental"]
    seasonality = analysis["seasonality"]
    company = analysis["company"]

    decision = decision_agent.decide(fundamental, seasonality)

    print("")
    print(company)
    print("Fundamental:", fundamental["conclusion"])
    print("Best month:", seasonality["best_month"]["month"])
    print("Decision:", decision["decision"])
    print("Score:", decision["score"])
    print("Reason:", decision["reason"])
    