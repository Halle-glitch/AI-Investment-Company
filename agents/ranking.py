class RankingAgent:

    def rank(self, analyses):

        ranked = sorted(
            analyses,
            key=lambda x: x["decision"]["score"],
            reverse=True
        )

        return ranked