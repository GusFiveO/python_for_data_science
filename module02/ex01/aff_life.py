from load_csv import load
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Use Tkinter backend


def aff_life():
    """aff_life"""
    life_expectancy_years = load("life_expectancy_years.csv")
    if life_expectancy_years is None:
        return None
    country_life_expectancy_list = life_expectancy_years.rows_by_key(
        key=["country"], named=True
    )
    x, y = zip(*country_life_expectancy_list["France"][0].items())
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_ylabel("Life expectancy")
    ax.set_xlabel("Year")
    ax.set_title("France Life expectancy Projections")
    labels = [str(year) for year in range(1800, 2100, 40)]
    ax.set_xticks(labels)
    plt.show(block=True)


if __name__ == "__main__":
    aff_life()
