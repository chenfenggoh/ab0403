import pandas as pd

# Load datasets
factsheet = pd.read_csv('factsheet.csv')
performance = pd.read_csv('performance.csv')

# Display the first few rows to understand structure
print(factsheet.head())
print(performance.head())

# Select relevant columns from the factsheet for ESG funds and sectors
funds = ['Narcissus Core Equity Sustainability Fund', 'Pietro Advisory Sustainable Large Cap ETF']
sectors = ['Energy', 'Utilities', 'Materials', 'Information Technology', 'Financials', 
           'Health Care', 'Consumer Staples', 'Consumer Discretionary', 'Industrials', 'Real Estate']

# Filter sector allocation for both funds
fund_allocation = factsheet[funds + sectors]

# Filter sector performance data
sector_performance = performance[sectors]

# Calculate the weighted performance for each fund
for fund in funds:
    # Multiply the fund's sector allocations by the corresponding sector performances
    weighted_perf = (fund_allocation[fund] * sector_performance).sum(axis=1)
    print(f'Weighted performance of {fund}:')
    print(weighted_perf)

# Analyze performance by comparing with benchmarks (S&P, Dow Jones)
benchmark_perf = performance[['S&P', 'Dow Jones']]

# Compare fund performance to benchmark
for fund in funds:
    weighted_perf = (fund_allocation[fund] * sector_performance).sum(axis=1)
    comparison = weighted_perf - benchmark_perf.mean(axis=1)
    print(f'Outperformance/underperformance of {fund} compared to benchmarks:')
    print(comparison)

# Example comparison of P/E ratio (from factsheet)
pe_ratio_fund1 = factsheet[f'Narcissus Core Equity Sustainability Fund P/E Ratio']
pe_ratio_fund2 = factsheet[f'Pietro Advisory Sustainable Large Cap ETF P/E Ratio']
print('P/E Ratio Comparison:')
print(f'Narcissus Fund P/E: {pe_ratio_fund1.mean()}')
print(f'Pietro ETF P/E: {pe_ratio_fund2.mean()}')