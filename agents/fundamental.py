class FundamentalAnalyst:
    def analyse(self, company, revenue_growth, profit_margin, debt):


        if debt < 30:
            risk_level = "Low risk"
        elif debt >= 30 and debt <= 50:
            risk_level = "Medium risk"
        else:
            risk_level = "High risk"


        conclusion = ""
        if revenue_growth > 0 and profit_margin > 10 and debt < 50:
            conclusion = "Bullish"
        elif revenue_growth < 0 and profit_margin < 10 and debt > 50:
            conclusion = "Bearish"
        elif revenue_growth > 0 and profit_margin > 10 and risk_level == "High risk":
            conclusion = "Neutral"
        else:
            conclusion = "Neutral"


        reason = ""
        if revenue_growth > 0 and profit_margin > 10 and debt < 50:
            reason = "Strong growth, healthy margins and manageable debt."
        elif revenue_growth < 0 and profit_margin < 10 and debt > 50:
            reason = "Negative growth, weak margins and high debt."
        else:
            reason = "Mixed financial indicators."


        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "debt": debt,
            "risk_level": risk_level,
            "reason": reason,
            "conclusion": conclusion
         
        }



   