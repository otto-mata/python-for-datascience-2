from load_csv import load
import re
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def parse_num(x: str) -> float:
    """Parse a number in locale format (letter suffixes) to integer"""
    mult = {"k": 1e3, "M": 1e6, "B": 1e9}
    if pd.isna(x):
        return float("nan")
    s = str(x).strip()

    m = re.fullmatch(r"([0-9]*\.?[0-9]+)\s*([kMB])?", s)
    if not m:
        return float("nan")

    val = float(m.group(1))
    unit = m.group(2)
    return val * (mult.get(unit, 1.0))


def main():
    """Plot the correlation between the life expectancy of the population and
    the gross domestic product of all the contries for the year 1900."""
    df_gdp_raw = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    df_le_raw = load("life_expectancy_years.csv")
    if df_le_raw is None or df_gdp_raw is None:
        exit(1)

    df_gdp = df_gdp_raw.melt("country", var_name="year", value_name="gdp")
    df_gdp["gdp"] = df_gdp["gdp"].map(parse_num)
    df_le = df_le_raw.melt("country", var_name="year", value_name="le")
    df_le["le"] = df_le["le"].map(parse_num)

    x_df = pd.merge(df_gdp, df_le, on=["country", "year"]).dropna()
    x_df["year"] = x_df["year"].astype(int)
    data = x_df[x_df["year"] == 1900].reset_index().drop("year", axis=1)
    ax = sns.scatterplot(
        data=data,
        x="gdp",
        y="le",
    )
    ax.set(xscale="log")
    ax.xaxis.set_major_formatter(lambda x, _: f"{int(x//1_000)}k")
    ax.set_ylabel(  # pyright: ignore[reportUnknownMemberType]
        "Life Expectancy",
    )
    ax.set_xlabel(  # pyright: ignore[reportUnknownMemberType]
        "Gross domestic product",
    )
    ax.set_title(  # pyright: ignore[reportUnknownMemberType]
        "1900",
    )
    plt.show()  # pyright: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main()
