import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Load the life expectancy dataset and display France's data.
    """
    # Load csv
    df = load("../ex00/life_expectancy_years.csv")

    if df is None:
        print("Error: Could not load the dataset.")
        return

    france_data = df[df['country'] == 'France']

    if france_data.empty:
        print("Error: France not found in the dataset.")
        return

    years = [int(col) for col in df.columns[1:]]
    life_expectancy = france_data.iloc[0, 1:].values

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(years, life_expectancy, linewidth=2, color='blue')
    plt.title("France Life Expectancy Projections", fontsize=16,
              fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy (years)", fontsize=12)

    # pour avoir tout les 40 ans comme l'exemple
    plt.xticks(range(min(years), max(years) + 1, 40))

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
