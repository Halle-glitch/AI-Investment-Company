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

def print_investment_report(analysis):

    company = analysis["company"]
    fundamental = analysis["fundamental"]
    seasonality = analysis["seasonality"]
    decision = analysis["decision"]

    print("")
    print("==============================")
    print(company)
    print("==============================")
    print("Fundamental:", fundamental["conclusion"])
    print("Fundamental Score:", fundamental["fundamental_score"])
    print("Best Month:", seasonality["best_month"]["month"])
    print("Seasonality Score:", round(
        seasonality["best_month"]["seasonality_score"], 2
    ))
    print("Decision Score:", decision["score"])
    print("Decision:", decision["decision"])
    print("Reason:", decision["reason"])

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
        fundamental_result = fundamental_analyst.analyse(
            "Company A", 15, 20, 20, 10
        )

    elif company == "Company B":
        fundamental_result = fundamental_analyst.analyse(
            "Company B", -8, 3, 70, -10
        )

    decision = decision_agent.decide(
        fundamental_result,
        seasonality_result
    )

    company_analysis = {
        "company": company,
        "seasonality": seasonality_result,
        "fundamental": fundamental_result,
        "decision": decision
    }

    analyses.append(company_analysis)

for analysis in analyses:
    print_investment_report(analysis)