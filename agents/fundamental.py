class FundamentalAnalyst:
    def analyse(self, company, revenue_growth):
        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "conclusion": "Bullish" if revenue_growth > 0 else "Bearish"
        }