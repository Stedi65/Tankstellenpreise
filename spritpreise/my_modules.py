import pandas as pd
import matplotlib.pyplot as plt
from db_functions import read_from_db
from os import system, name


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def average_prices(datetime1: str, datetime2: str, fuel_typ: str) -> list:
    sql = f"select name, round(avg({fuel_typ}),2) as price from daten GROUP by id".replace("\n", "")
    price_list = read_from_db(sql)
    return price_list


def _float(value) -> float:
    if type(value) == float:
        return value
    if type(value) != str:
        return 0.00
    return float(value)


def print_output(text: str) -> None:
    print(text)


def Chart_of_patrol_stations(date1: str, date2: str, fuel_typ: str) -> None:
    sql = f"SELECT id, name, {fuel_typ} FROM 'daten' ORDER BY id"
    sql = sql.replace("\n", "")
    price_list = read_from_db(sql)
    c = []
    for x in range(len(price_list)):
        if price_list[x][0] not in c:
            c.append((price_list[x][0], price_list[x][1], price_list[x][2]))
    patrol_stations = len(c)
    print(patrol_stations)
    df = pd.DataFrame(price_list)
    df = df.set_index(df.columns[0])
    df.columns = ['Name', 'Preis']
    for i in range(patrol_stations):
        xx = df[df.Name == c[i]]
        plt.plot(xx.Name, xx.Preis )

    plt.xlabel("Preis")
    plt.title(f"Spritpreisentwicklung für {fuel_typ.upper()}")
    plt.show()


def Chart_of_average_prices(date1: str, date2: str, fuel_typ) -> None:
    price_list = average_prices(date1, date2, fuel_typ)
    df = pd.DataFrame(price_list)
    df = df.set_index(df.columns[0])
    df = df.sort_values(by=[1], ascending=False)
    df.plot.bar()
    plt.xlabel("Preis in €")
    plt.xticks(rotation=45)
    plt.title(f"Durchschnittspreise für {fuel_typ.upper()}")
    plt.show()
