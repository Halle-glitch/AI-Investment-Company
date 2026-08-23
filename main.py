from agents.seasonality import SeasonalityAnalyst
from agents.fundamental import FundamentalAnalyst
from agents.decision import DecisionAgent
from agents.risk import RiskAgent
from agents.ranking import RankingAgent
from agents.recommendation import RecommendationAgent


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
    risk = analysis["risk"]

    print("")
    print("==============================")
    print(company)
    print("==============================")
    print("Fundamental:", fundamental["conclusion"])
    print("Fundamental Score:", fundamental["fundamental_score"])
    print("Risk:", risk["risk_level"])
    print("Risk Score:", risk["risk_score"])
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
risk_agent = RiskAgent()
ranking_agent = RankingAgent()
recommendation_agent = RecommendationAgent()

companies = [
    {
        "name": "Company A",
        "revenue_growth": 15,
        "profit_margin": 20,
        "debt": 20,
        "eps_growth": 10
    },
    {
        "name": "Company B",
        "revenue_growth": -8,
        "profit_margin": 3,
        "debt": 70,
        "eps_growth": -10
    }
]

analyses = []

for company in companies:

    company_name = company["name"]

    seasonality_result = seasonality_analyst.analyse_company(company_name)

    fundamental_result = fundamental_analyst.analyse(
        company_name,
        company["revenue_growth"],
        company["profit_margin"],
        company["debt"],
        company["eps_growth"]
    )

    risk_result = risk_agent.analyse(fundamental_result)

    decision = decision_agent.decide(
        fundamental_result,
        seasonality_result,
        risk_result
    )

    company_analysis = {
    "company": company_name,
    "seasonality": seasonality_result,
    "fundamental": fundamental_result,
    "risk": risk_result,
    "decision": decision
    }

    analyses.append(company_analysis)

for analysis in analyses:
    print_investment_report(analysis)

ranked = ranking_agent.rank(analyses)

recommendation = recommendation_agent.recommend(ranked)

print("")
print("==============================")
print("TOP INVESTMENT")
print("==============================")

if recommendation:

    print("Company:", recommendation["company"])
    print("Decision:", recommendation["decision"]["decision"])
    print("Score:", recommendation["decision"]["score"])

else:
    print("No BUY recommendation.")

