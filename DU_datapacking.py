import pickle

countries = {}

def add_country(country, capital):
    countries[country] = capital
    print(f"{country} with capital {capital} was added.")


def delete_country(country):
    if country in countries:
        del countries[country]
        print(f"{country} was deleted.")
    else:
        print(f"{country} not found.")


def find_country(country):
    return countries.get(country, "Country not found.")


def edit_country(country, new_capital):
    if country in countries:
        countries[country] = new_capital
        print(f"{country} capital updated to {new_capital}.")
    else:
        print(f"{country} not found.")


def save_data(filename="tests.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(countries, file)
    print("Data saved.")


def load_data(filename="tests.pickle"):
    global countries
    try:
        with open(filename, "rb") as file:
            countries = pickle.load(file)
        print("Data loaded.")
    except FileNotFoundError:
        print("No saved data found.")


add_country("Slovakia", "Bratislava")
add_country("Czech Republic", "Prague")
edit_country("Slovakia", "New Bratislava")
delete_country("Czech Republic")

save_data("tests.pickle")
load_data("tests.pickle")

print(countries)