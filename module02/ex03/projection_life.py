from load_csv import load
import matplotlib
from matplotlib import ticker
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Use Tkinter backend


def projection_life():
    """projection life"""
    life_expectancy_years = load("life_expectancy_years.csv")
    if life_expectancy_years is None:
        return None
    income_per_person = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    if income_per_person is None:
        return None

    columns = ["country", "1900"]

    income_per_person = income_per_person[columns].dropna()

    life_expectancy_1900 = life_expectancy_years[columns].dropna()
    life_expectancy_1900_countries = life_expectancy_1900["country"]
    life_expectancy_1900_values = life_expectancy_1900["1900"]
    life_expectancy_list = life_expectancy_1900_values.tolist()

    filtered_income = income_per_person[
        income_per_person["country"].isin(
            life_expectancy_1900_countries.tolist())
    ]
    income_per_person_list = filtered_income["1900"].tolist()

    fig, ax = plt.subplots()
    ax.scatter(income_per_person_list, life_expectancy_list)
    ax.set_title("1900")
    ax.set_ylabel("Life Expectancy")
    ax.set_xlabel("Gross domestic product")
    ax.set_xscale("log")
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(['300', '1K', '10K'])
    plt.show()


if __name__ == "__main__":
    projection_life()
