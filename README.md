# AI Investment Company

A Python project that analyses companies using multiple investment agents.

## Current Agents

### Fundamental Analyst
Analyses:
- Revenue growth
- Profit margin
- Debt
- EPS growth

Returns:
- Risk level
- Conclusion

### Seasonality Analyst
Analyses:
- Monthly historical returns
- Average return
- Positive years
- Volatility
- Seasonality score

Finds:
- Best month
- Worst month

### Decision Agent
Combines:
- Fundamental analysis
- Seasonality analysis

Returns:
- BUY
- HOLD
- SELL

## Current Project Structure

AI-Investment-Company/
│
├── agents/
│   ├── fundamental.py
│   ├── seasonality.py
│   └── decision.py
│
├── data/
│   └── seasonality_data.py
│
└── main.py