from agents.fundamental import FundamentalAnalyst
from agents.seasonality import SeasonalityAnalyst

print("AI Investment Company")

analyst = FundamentalAnalyst()

resultA = analyst.analyse("Company A", 15, 20, 20, 10)
resultB = analyst.analyse("Company B", -8, 3, 70, -10)
resultC = analyst.analyse("Company C", 12, 5, 30, 0)
resultD = analyst.analyse("Company D", 5, 12, 60, 8)
resultE = analyst.analyse("Company E", -5, 15, 20, -2)
resultF = analyst.analyse("Company F", -5, 15, 70, -2)

print(resultA)
print(resultB)
print(resultC)
print(resultD)
print(resultE)
print(resultF)
print("")
print("")
print("")
print("")


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

results = []

for month in months:
    result = analyst.analyse("Company A", month)
    results.append(result)
print(results)



best_month = None

for result in results:
    if best_month is None or result["average_return"] > best_month["average_return"]:
        best_month = result


worst_month = None

for result in results:
    if worst_month is None or result["average_return"] < worst_month["average_return"]:
        worst_month = result


highest_return = None

for result in results:
    if highest_return is None or result["average_return"] > highest_return["average_return"]:
        highest_return = result


lowest_return = None

for result in results:
    if lowest_return is None or result["average_return"] < lowest_return["average_return"]:
        lowest_return = result        


for result in results:

    return_score = (
        (result["average_return"] - lowest_return["average_return"])
        /
        (highest_return["average_return"] - lowest_return["average_return"])
    ) * 100

    consistency_score = result["positive_year_percentage"]

    stability_score = min(100,max(0, 100 - (result["volatility"] * 10)))

    seasonality_score = ((return_score * 0.40) + (consistency_score * 0.40) + (stability_score * 0.20))
    
    result["return_score"] = return_score
    result["consistency_score"] = consistency_score
    result["stability_score"] = stability_score
    result["seasonality_score"] = seasonality_score

    print(
    result["month"],
    "Return:", round(return_score, 2),
    "Consistency:", round(consistency_score, 2),
    "Stability:", round(stability_score, 2),
    "Score:", round(seasonality_score, 2)
)


print("Best month:", best_month["month"])
print("Worst month:", worst_month["month"])
print("Highest return:", highest_return)
print("Lowest return:", lowest_return)