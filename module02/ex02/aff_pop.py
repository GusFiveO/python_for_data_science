from load_csv import load
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
matplotlib.use('TkAgg')  # Use Tkinter backend


def aff_pop():
    """aff_pop"""
    population_total = load("population_total.csv")
    if population_total is None:
        return None

    population_total = population_total.select(
        ["country"] + [str(year) for year in range(1800, 2050)]
    )

    population_total_by_country = population_total.rows_by_key(
        key=["country"], named=True
    )

    years_, france_population = zip(
        *population_total_by_country["France"][0].items())
    years_, belgium_population = zip(
        *population_total_by_country["Belgium"][0].items())

    years = [str(year) for year in range(1800, 2050, 40)]

    france_population = [float(pop[:-1]) for pop in france_population]
    belgium_population = [float(pop[:-1]) for pop in belgium_population]

    fig, ax = plt.subplots()
    ax.plot(years_, france_population)
    ax.plot(years_, belgium_population)
    ax.set_title("Population Projections")
    ax.set_ylabel("Population")
    ax.set_xlabel("Year")
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.0fM"))
    ax.xaxis.set_ticks(years)
    ax.yaxis.set_ticks([pop for pop in range(20, 80, 20)])
    ax.legend(["Belgium", "France"], loc="lower right")
    plt.show()


if __name__ == "__main__":
    aff_pop()
