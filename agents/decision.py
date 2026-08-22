class DecisionAgent:

    def decide(self, fundamental, seasonality):

        conclusion = fundamental["conclusion"]
        season = seasonality["best_month"]["seasonality_score"]

        if conclusion == "Bullish" and season >= 60:
            return {
                "decision": "BUY",
                "reason": "Bullish fundamentals and strong seasonality."
            }

        elif conclusion == "Bearish" and season < 60:
            return {
                "decision": "SELL",
                "reason": "Bearish fundamentals and weak seasonality."
            }

        else:
            return {
                "decision": "HOLD",
                "reason": "Signals are mixed."
            }