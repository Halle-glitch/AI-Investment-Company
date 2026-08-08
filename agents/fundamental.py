class FundamentalAnalyst:
    def analyse(self, company, revenue_growth, profit_margin, debt):
        conclusion = "0"
        if revenue_growth > 0 and profit_margin > 10 and debt < 50:
            conclusion = "Bullish"
        elif revenue_growth < 0 and profit_margin < 10 and debt > 50:
            conclusion = "Bearish"
        else:
            conclusion = "Neutral"

        
        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "debt": debt,
            "conclusion": conclusion  
        }



   