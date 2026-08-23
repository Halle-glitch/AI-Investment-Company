class RiskAgent:

    def analyse(self, fundamental):

        risk_level = fundamental["risk_level"]

        if risk_level == "Low risk":
            risk_score = 100
            reason = "Low financial risk."

        elif risk_level == "High risk":
            risk_score = 0
            reason = "High financial risk."

        else:
            risk_score = 50
            reason = "Moderate financial risk."

        return {
            "risk_level": risk_level,
            "risk_score": risk_score,
            "reason": reason
        }