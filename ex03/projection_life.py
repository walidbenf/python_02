import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
import numpy as np


def clean_gdp_data(gdp_value):
    """Clean GDP data by removing 'k' suffix and converting to numeric."""
    if pd.isna(gdp_value):
        return np.nan

    gdp_str = str(gdp_value)
    if gdp_str.endswith('k'):
        return float(gdp_str[:-1]) * 1000
    else:
        return float(gdp_str)


def main():
    """
    Load GDP and life expectancy datasets and create a scatter plot
    showing the relationship for the year 1900.
    """
    # Load both CSV files
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("../ex00/life_expectancy_years.csv")

    if gdp_df is None or life_df is None:
        print("Error: Could not load one or both datasets.")
        return

    year = "1900"

    if year not in gdp_df.columns or year not in life_df.columns:
        print(f"Error: Year {year} not found in the datasets.")
        return

    gdp_1900 = gdp_df[['country', year]].copy()
    life_1900 = life_df[['country', year]].copy()

    gdp_1900.columns = ['country', 'gdp']
    life_1900.columns = ['country', 'life_expectancy']

    merged_data = pd.merge(gdp_1900, life_1900, on='country', how='inner')

    merged_data['gdp_clean'] = merged_data['gdp'].apply(clean_gdp_data)

    merged_data['life_expectancy_numeric'] = pd.to_numeric(
        merged_data['life_expectancy'], errors='coerce')

    clean_data = merged_data.dropna(
        subset=['gdp_clean', 'life_expectancy_numeric'])

    if clean_data.empty:
        print("Error: No valid data available for the year 1900.")
        return

    plt.figure(figsize=(10, 6))
    plt.scatter(clean_data['gdp_clean'], clean_data['life_expectancy_numeric'],
                alpha=0.7, s=50, color='blue')

    plt.title("1900", fontsize=14, fontweight='bold')
    plt.xlabel("Gross domestic product", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)

    plt.xscale('log')

    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
