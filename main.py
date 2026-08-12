from agents.fundamental import FundamentalAnalyst

print("AI Investment Company")

analyst = FundamentalAnalyst()

result = analyst.analyse("Microsoft", 12, 15, 20, -5)
result1 = analyst.analyse("Microsoft", -5, 5, 70,0)
result2 = analyst.analyse("Microsoft", 12, 5, 30,0)
result3 = analyst.analyse("Microsoft", 12, 15, 70,0)
result4 = analyst.analyse("Microsoft", 12, 15, 20, 0)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)


