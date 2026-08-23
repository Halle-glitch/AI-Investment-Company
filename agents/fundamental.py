class FundamentalAnalyst:

    # Check if the company has strong fundamentals
    def strong_fundamentals(self, revenue_growth, profit_margin):
        if revenue_growth > 0 and profit_margin > 10:
            return True
        else:
            return False

    # Check if the company has weak fundamentals
    def weak_fundamentals(self, revenue_growth, profit_margin):
        if revenue_growth < 0 and profit_margin < 10:
            return True
        else:
            return False

    def analyse(self, company, revenue_growth, profit_margin, debt, eps_growth):

        fundamental_score = 0

        if revenue_growth > 10:
            fundamental_score += 25

        if profit_margin > 10:
            fundamental_score += 25

        if debt < 30:
            fundamental_score += 25

        if eps_growth > 5:
            fundamental_score += 25

        # Determine the company's risk level
        if debt < 30 and profit_margin > 5: 
            risk_level = "Low risk"

        elif debt > 50 or profit_margin < 5:
            risk_level = "High risk"

        else:
            risk_level = "Medium risk"


        # Check the company's fundamental strength
        strong = self.strong_fundamentals(
            revenue_growth,
            profit_margin
        )

        weak = self.weak_fundamentals(
            revenue_growth,
            profit_margin
        )


        # Determine the investment conclusion
        if strong and risk_level == "High risk":
            conclusion = "Neutral"

        elif strong:
            conclusion = "Bullish"

        elif weak:
            conclusion = "Bearish"

        else:
            conclusion = "Neutral"


        # Generate a reason for the conclusion
        reason = ""

        if strong and risk_level == "High risk":
            reason = "Fundamentals are strong, but risk is high."

        elif strong and eps_growth > 0:
            reason = "Strong growth, healthy margins and manageable debt."

        elif strong and eps_growth < 0:
            reason = "Strong fundamentals despite negative EPS growth."

        elif strong and eps_growth == 0:
            reason = "Strong fundamentals with stable EPS growth."

        elif revenue_growth < 0 and profit_margin > 10 and risk_level == "High risk":
            reason = "Negative growth, healthy profit margin and high debt."

        elif revenue_growth < 0 and profit_margin > 10 and risk_level == "Low risk":
            reason = "Negative growth, healthy profit margin and low debt."

        elif weak:
            reason = "Negative growth, weak margins and high debt."

        else:
            reason = "Mixed financial indicators."


        # Return all analysis results
        return {
            "company": company,
            "revenue_growth": revenue_growth,
            "profit_margin": profit_margin,
            "debt": debt,
            "eps_growth": eps_growth,
            "risk_level": risk_level,
            "fundamental_score": fundamental_score,
            "reason": reason,
            "conclusion": conclusion 
        }