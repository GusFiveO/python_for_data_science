from load_csv import load
import pandas
import matplotlib.pyplot as plt

def projection_life():
	"""projection life"""
	life_expectancy_years = load("life_expectancy_years.csv")
	income_per_person = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

	columns = ["country", "1900"]

	income_per_person = income_per_person[columns].dropna()

	life_expectancy_1900 = life_expectancy_years[columns].dropna()
	life_expectancy_1900_countries = life_expectancy_1900["country"]
	life_expectancy_1900_values = life_expectancy_1900["1900"]
	life_expectancy_list = life_expectancy_1900_values.tolist()

	filtered_income = income_per_person[income_per_person["country"].isin(life_expectancy_1900_countries.tolist())]
	income_per_person_list = filtered_income["1900"].tolist()

	fig, ax = plt.subplots()
	ax.scatter(income_per_person_list, life_expectancy_list)
	plt.show()

if __name__ == "__main__":
	projection_life()
