from agents.fundamental import FundamentalAnalyst

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