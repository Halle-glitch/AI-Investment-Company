import statistics
from data.seasonality_data import seasonality_data


class SeasonalityAnalyst:

    # Analyse the historical performance of a month
    def analyse(self, company, month):

        # Get the historical returns for the selected month
        historical_returns = seasonality_data[month]

        # Calculate the average return
        average_return = sum(historical_returns) / len(historical_returns)

        # Count how many years had a positive return
        positive_years = 0

        for i in historical_returns:
            if i > 0:
                positive_years += 1

        # Calculate the percentage of positive years
        positive_year_percentage = (positive_years / len(historical_returns)) * 100

        # Count negative years
        negative_years = len(historical_returns) - positive_years

        # Calculate the percentage of negative years
        negative_year_percentage = (negative_years / len(historical_returns)) * 100

        # Calculate how much the returns vary from year to year
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