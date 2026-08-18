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


    def calculate_scores(self, results):
        highest_return = None
        lowest_return = None

        for result in results:
            if highest_return is None or result["average_return"] > highest_return["average_return"]:
                highest_return = result

            if lowest_return is None or result["average_return"] < lowest_return["average_return"]:
                lowest_return = result

        for result in results:

            return_score = ((result["average_return"] - lowest_return["average_return"]) / (highest_return["average_return"] - lowest_return["average_return"])) * 100

            consistency_score = result["positive_year_percentage"]

            stability_score = min(100,max(0, 100 - (result["volatility"] * 10)))

            seasonality_score = ((return_score * 0.40)+ (consistency_score * 0.40)+ (stability_score * 0.20))

            result["return_score"] = return_score
            result["consistency_score"] = consistency_score
            result["stability_score"] = stability_score
            result["seasonality_score"] = seasonality_score

        return results


    def find_best_month(self, results):

        best_month = None

        for result in results:
            if best_month is None or result["seasonality_score"] > best_month["seasonality_score"]:
                best_month = result

        return best_month


    def find_worst_month(self, results):

        worst_month = None

        for result in results:
            if worst_month is None or result["seasonality_score"] < worst_month["seasonality_score"]:
                worst_month = result

        return worst_month


    def analyse_company(self, company):

        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        results = []

        for month in months:
            result = self.analyse(company, month)
            results.append(result)

        results = self.calculate_scores(results)

        best_month = self.find_best_month(results)
        worst_month = self.find_worst_month(results)
        
        return {
            "results": results,
            "best_month": best_month,
            "worst_month": worst_month
            }
    