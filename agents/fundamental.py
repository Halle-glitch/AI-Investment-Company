class FundamentalAnalyst:
    def strong_fundamentals(self, revenue_growth, profit_margin, debt):
        if revenue_growth > 0 and profit_margin > 10 and debt < 50:
            return True
        else:
            return False

    def weak_fundamentals(self, revenue_growth, profit_margin, debt):
        if revenue_growth < 0 and profit_margin < 10 and debt > 50:
            return True
        else:
            return False

    def analyse(self, company, revenue_growth, profit_margin, debt, eps_growth):

        if debt < 30:
            risk_level = "Low risk"

        elif debt >= 30 and debt <= 50:
            risk_level = "Medium risk"
        else:
            risk_level = "High risk"


        strong = self.strong_fundamentals(revenue_growth, profit_margin, debt)
        weak = self.weak_fundamentals(revenue_growth, profit_margin, debt)

        if strong and risk_level == "High risk":
            conclusion = "Neutral"

        elif strong:
            conclusion = "Bullish"

        elif weak:
            conclusion = "Bearish"

        else:
            conclusion = "Neutral"
            

        #conclusion = ""
        #if revenue_growth > 0 and profit_margin > 10 and debt < 50:
            #conclusion = "Bullish"
        #elif revenue_growth < 0 and profit_margin < 10 and debt > 50:
            #conclusion = "Bearish"
        #elif revenue_growth > 0 and profit_margin > 10 and risk_level == "High risk":
            #conclusion = "Neutral"
        #else:
           # onclusion = "Neutral" 


        
        reason = ""
        if revenue_growth > 0 and profit_margin > 10 and debt < 50 and eps_growth > 0:
            reason = "Strong growth, healthy margins and manageable debt."
        elif revenue_growth > 0 and profit_margin > 10 and debt < 50 and eps_growth < 0:
            reason = "Strong fundamentals despite negative EPS growth."
        elif revenue_growth < 0 and profit_margin < 10 and debt > 50:
            reason = "Negative growth, weak margins and high debt."
        else:
            reason = "Mixed financial indicators."


        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "debt": debt,
            "eps_growth": eps_growth,
            "risk_level": risk_level,
            "reason": reason,
            "conclusion": conclusion
         
        }



   