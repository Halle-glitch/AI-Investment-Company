
class DecisionAgent:

    def decide(self, fundamental, seasonality):

        conclusion = fundamental["conclusion"]
        season = seasonality["best_month"]["seasonality_score"]

        if conclusion == "Bullish" and season >= 60:
            return "BUY"
        else:
            return "HOLD"