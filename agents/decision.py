class DecisionAgent:

    def decide(self, fundamental, seasonality):

        conclusion = fundamental["conclusion"]
        season = seasonality["best_month"]["seasonality_score"]
        risk = fundamental["risk_level"]
        fundamental_score = fundamental["fundamental_score"]

        risk_score = 0

        if risk == "Low risk":
            risk_score = 100
        elif risk == "High risk":
            risk_score = 0

        decision_score = (fundamental_score * 0.4 + season * 0.4 + risk_score * 0.2)

        if conclusion == "Bullish" and decision_score >= 60:
            return {
                "decision": "BUY",
                "reason": "Bullish fundamentals and strong seasonality.",
                "score": round(decision_score, 2)
            }

        elif conclusion == "Bearish" and decision_score < 40:
            return {
                "decision": "SELL",
                "reason": "Bearish fundamentals and weak seasonality.",
                "score": round(decision_score, 2)
            }

        else:
            return {
                "decision": "HOLD",
                "reason": "Signals are mixed.",
                "score": round(decision_score, 2)
            }