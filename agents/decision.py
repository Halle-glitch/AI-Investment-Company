class DecisionAgent:

    def decide(self, fundamental, seasonality, risk):

        conclusion = fundamental["conclusion"]
        season = seasonality["best_month"]["seasonality_score"]
        fundamental_score = fundamental["fundamental_score"]
        risk_score = risk["risk_score"]


        decision_score = (fundamental_score * 0.4 + season * 0.4 + risk_score * 0.2)

        if conclusion == "Bullish" and decision_score >= 60:
            return {
                "decision": "BUY",
                "reason": "Bullish fundamentals, strong seasonality and acceptable risk.",
                "score": round(decision_score, 2)
                }

        elif conclusion == "Bearish" and decision_score < 40:
            return {
                "decision": "SELL",
                "reason": "Bearish fundamentals and high risk outweigh seasonality.",
                "score": round(decision_score, 2)
                }

        else:
            return {
            "decision": "HOLD",
            "reason": "Signals are mixed.",
            "score": round(decision_score, 2)
            }