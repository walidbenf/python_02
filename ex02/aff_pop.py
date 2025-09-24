import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Load the population dataset and compare France with another country.
    Display data from 1800 to 2050.
    """
    # Load csv
    df = load("population_total.csv")

    if df is None:
        print("Error: Could not load the dataset.")
        return

    # Countries to compare(can change the country to test)
    country1 = "France"
    country2 = "Belgium"

    france_data = df[df['country'] == country1]
    other_country_data = df[df['country'] == country2]

    if france_data.empty:
        print(f"Error: {country1} not found in the dataset.")
        return

    if other_country_data.empty:
        print(f"Error: {country2} not found in the dataset.")
        return

    # Get all year columns (assuming years from 1800 to 2050)
    year_columns = [col for col in df.columns[1:] if col.isdigit()]
    years = [int(col) for col in year_columns]
    filtered_years = [year for year in years if 1800 <= year <= 2050]
    filtered_columns = [str(year) for year in filtered_years]

    # Extract population data
    france_population = france_data[filtered_columns].iloc[0].values
    other_population = other_country_data[filtered_columns].iloc[0].values
    france_population = [float(str(val).replace('M', ''))
                         for val in france_population]
    other_population = [float(str(val).replace('M', ''))
                        for val in other_population]

    # Create the plot
    plt.figure(figsize=(12, 8))

    plt.plot(filtered_years, france_population, linewidth=2,
             label=country1, color='green')
    plt.plot(filtered_years, other_population, linewidth=2,
             label=country2, color='blue')

    plt.title("Population Projections", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)

    plt.legend(loc='lower right', fontsize=10)

    # exemple tout les 40 ans
    plt.xticks(range(1800, 2051, 40))

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
