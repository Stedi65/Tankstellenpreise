import requests
from dataclasses import dataclass
from datetime import datetime
from db_functions import add_to_db, read_from_db
from my_modules import clear_screen, _float, print_output
from time import sleep, time
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_config() -> dict:
    try:
        with open(BASE_DIR / 'config.json', "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        # raise ConfigLoadError
        pass


def get_api_key(config) -> str:
    return config.get("key")


def get_rad(config) -> float:
    try:
        ret = float(config.get("rad"))
        return ret
    except TypeError:
        print_output("Falscher Wert für rad in der config.cfg")


def get_lat(config) -> float:
    try:
        ret = float(config.get("lat"))
        return ret
    except TypeError:
        print_output("Falscher Wert für lat in der config.cfg")


def get_lng(config) -> float:
    try:
        ret = float(config.get("lng"))
        return ret
    except TypeError:
        print_output("Falscher Wert für lng in der config.cfg")


def get_interval(config) -> int:
    try:
        ret = int(config.get("interval"))
        return ret
    except TypeError:
        print_output("Falscher Wert für interval in der config.cfg")


def get_response(key: str, lat: float, lng :float, rad: float):
    tankerkoenig_url = f"https://creativecommons.tankerkoenig.de/json/list.php?lat={lat}&lng={lng}&rad={rad}&sort=dist&type=all&apikey={key}"
    tankerkoenig_url = tankerkoenig_url.replace("\n", "")
    response = requests.get(tankerkoenig_url).json()
    if response.get("ok") == "True":
        raise ConnectionError(f"Connection Error {tankerkoenig_url}")
    return response


def get_petrol_stations(response: dict) -> list:
    return response.get("stations")


def write_stations_to_db(stations: list) -> None:
    for el in stations:
        id = el.get("id")
        name = el.get("name")
        brand = el.get("brand")
        street = el.get("street")
        place = el.get("place")
        lat = float(el.get("lat"))
        lng = float(el.get("lng"))
        dist = float(el.get("dist"))
        diesel = _float(el.get("diesel", "0.00"))
        e5 = _float(el.get("e5", "0.00"))
        e10 = _float(el.get("e10", "0.00"))
        if el.get("isOpen") == True:
            isOpen = 1
        else:
            isOpen = 0
        houseNumber = el.get("houseNumber")
        postCode = el.get("postCode")
        dt = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        #print_output(
        #    f"id = {id}\n name = {name}\n brand = {brand}\n"
        #    f"street = {street}\n place = {place}\n lat = {lat}\n"
        #    f"lng = {lng}\n dist = {dist}\n diesel = {diesel}\n"
        #    f"e5 = {e5}\n e10 = {e10}\n isOpen = {isOpen}\n"
        #    f"houseNumber = {houseNumber}\n postCode = {postCode}\n"
        #    f"dt = {dt}\n"
        #             )
        add_to_db(id, name, brand, street, place, lat, lng, dist, diesel, e5, e10, isOpen, houseNumber, postCode, dt)
        print_output(f"Datensatz für {name}, {place} in db gespeichert!")


@dataclass
class Activity:
    id: str
    name: str
    brand: str
    sreet: str
    place: str
    lat: float
    lng: float
    dist: float
    diesel: float
    e5: float
    e10: float
    isOpen: bool
    houseNumber: str
    postcode: int
    datetime: str


# Einstellungen aus config.cfg laden
CONFIG = read_config()
api_key = get_api_key(CONFIG)
rad = get_rad(CONFIG)
lat = get_lat(CONFIG)
lng = get_lng(CONFIG)
interval = get_interval(CONFIG)

while True:
    start_time = round(time(), 0)
    resp = get_response(api_key, lat, lng, rad)
    stations = get_petrol_stations(resp)
    write_stations_to_db(stations)
    remaining_time = interval - (round(time(), 0) - start_time)
    while round(time(), 0) - start_time < interval:
        if remaining_time > 60:
            sleep(60)
        else:
            sleep(remaining_time)
        remaining_time = interval - (round(time(), 0) - start_time)
        clear_screen()
        print_output(f"Restzeit bis zum nächsten Request: {remaining_time}")

