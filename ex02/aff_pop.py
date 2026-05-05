from load_csv import load
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd
import re


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
    """Plot the population projection of the countries of France and Belgium"""
    df = load("population_total.csv")
    if df is None:
        exit(1)
    df = df[df["country"].isin(["France", "Belgium"])].melt(
        "country", var_name="year", value_name="population_raw"
    )
    df["year"] = df["year"].astype(int)
    df["population"] = df["population_raw"].map(parse_num)
    df = df[df["year"].between(1800, 2050)].copy()
    ax = sns.lineplot(df, x="year", y="population", hue="country")
    ax.set_xlim(1800, 2050)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_formatter(lambda y, _: f"{y/1_000_000:.0f}M")
    ax.set_ylabel(  # pyright: ignore[reportUnknownMemberType]
        "Population",
    )
    ax.set_xlabel("Year")  # pyright: ignore[reportUnknownMemberType]
    ax.set_title(  # pyright: ignore[reportUnknownMemberType]
        "Population Projections",
    )
    plt.show()  # pyright: ignore[reportUnknownMemberType]


if __name__ == "__main__":
    main()
