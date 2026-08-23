class RecommendationAgent:

    def recommend(self, ranked):

        for analysis in ranked:

            decision = analysis["decision"]["decision"]

            if decision == "BUY":
                return analysis

        return None