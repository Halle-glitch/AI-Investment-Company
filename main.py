from agents.fundamental import FundamentalAnalyst

print("AI Investment Company")

analyst = FundamentalAnalyst()

result = analyst.analyse("Microsoft", -5)
print(result)