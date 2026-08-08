class FundamentalAnalyst:
    def analyse(self, company, revenue_growth, profit_margin, debt):
        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "debt": debt,
            "conclusion": "Bullish" if revenue_growth > 0 and profit_margin > 10 and debt < 50 else "Bearish"
        }



   