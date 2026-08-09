from agents.fundamental import FundamentalAnalyst

print("AI Investment Company")

analyst = FundamentalAnalyst()

result = analyst.analyse("Microsoft", 12, 15, 20)
result1 = analyst.analyse("Microsoft", -5, 5, 70)
result2 = analyst.analyse("Microsoft", 12, 5, 30)
result3 = analyst.analyse("Microsoft", 12, 15, 70)
print(result)
print(result1)
print(result2)
print(result3)
