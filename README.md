# Clickstream Session Analysis

A Python script that analyzes website event logs (page views, add-to-cart, purchases) to answer common web analytics questions about user behavior.

## What it calculates
- **Events per session**: how many actions each visitor took
- **Session duration**: time between the first and last event of each session
- **Page popularity**: which pages get the most views
- **Conversion rate**: the share of sessions that ended in a purchase

## How to run
```bash
python session_analysis.py
```

## What I learned
- Converting timestamp strings with `pd.to_datetime()` so time arithmetic works
- Using `.groupby()` with `.size()` and `.agg(['min', 'max'])` to summarize data per session
- Calculating durations by subtracting datetimes and using `.dt.total_seconds()`
- Using `.value_counts()` for quick frequency rankings
- Using `.unique()` and `.nunique()` to count distinct sessions for a conversion rate

## Dependencies
Requires pandas:
```bash
pip install pandas
```
