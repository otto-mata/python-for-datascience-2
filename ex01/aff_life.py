from load_csv import load
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def main():
    """Plot data from a CSV file representing
    the life expectancy of the population."""
    df = load("life_expectancy_years.csv")
    if df is None:
        exit(1)
    df = df[df["country"] == "France"].melt(
        "country", var_name="year", value_name="expectancy"
    )
    sns.set_theme("notebook")
    ax = sns.lineplot(df, x="year", y="expectancy")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.set_ylabel(  # pyright: ignore[reportUnknownMemberType]
        "Life Expectancy",
    )
    ax.set_xlabel("Year")  # pyright: ignore[reportUnknownMemberType]
    ax.set_title(  # pyright: ignore[reportUnknownMemberType]
        "France Life Expectancy Projections",
    )
    plt.show()  # pyright: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main()
