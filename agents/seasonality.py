import statistics


class SeasonalityAnalyst:
    def analyse(self, company, month, historical_returns):
        average_return = sum(historical_returns) / len(historical_returns)

        positive_years = 0 
        for i in historical_returns:
            if i > 0:
                positive_years += 1
        positive_year_percentage = (positive_years / len(historical_returns)) * 100

        negative_years = len(historical_returns) - positive_years

        negative_year_percentage = (negative_years / len(historical_returns)) * 100

        volatility = statistics.stdev(historical_returns)

        return {
        "company": company,
        "month": month,
        "historical_returns": historical_returns,
        "average_return": average_return,
        "positive_years": positive_years,
        "positive_year_percentage": positive_year_percentage, 
        "negative_years": negative_years,
        "negative_year_percentage": negative_year_percentage,
        "volatility": volatility
        }