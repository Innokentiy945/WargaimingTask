import random
import shutil
import sqlite3
import os
import pytest

from db_original_creating_service import DBOriginalInit

def ensure_original_db_created():
    random.seed()
    if os.path.exists("shipsOriginal.db"):
        os.remove("shipsOriginal.db")
    conn = sqlite3.connect("shipsOriginal.db")
    db = DBOriginalInit(conn)
    db.create_tables()
    db.insert_to_weapons()
    db.insert_to_hulls()
    db.insert_to_engines()
    db.insert_to_ships()
    db.close()

def ensure_temp_db_created():
    random.seed()
    if os.path.exists("shipsTemp.db"):
        os.remove("shipsTemp.db")
    shutil.copy("shipsOriginal.db", "shipsTemp.db")
    conn = sqlite3.connect("shipsTemp.db")
    cursor = conn.cursor()

    cursor.execute("SELECT ship, weapon, hull, engine FROM Ships")
    ships = cursor.fetchall()

    for row in ships:
        ship_name = row[0]
        ship_component = random.choice(["weapon", "hull", "engine"])

        if ship_component == "weapon":
            new_value = f"Weapon-{random.randint(1, 20)}"
            cursor.execute("UPDATE Ships SET weapon = ? WHERE ship = ?", (new_value, ship_name))
        elif ship_component == "hull":
            new_value = f"Hull-{random.randint(1, 5)}"
            cursor.execute("UPDATE Ships SET hull = ? WHERE ship = ?", (new_value, ship_name))
        else:
            new_value = f"Engine-{random.randint(1, 6)}"
            cursor.execute("UPDATE Ships SET engine = ? WHERE ship = ?", (new_value, ship_name))

    conn.commit()
    conn.close()

def pytest_generate_tests(metafunc):
    fixtures = metafunc.fixturenames
    if not all(name in fixtures for name in ["ship", "ship_component", "original_value", "current_value"]):
        return

    ensure_original_db_created()
    ensure_temp_db_created()

    original_data = load_ship_data_from_db("shipsOriginal.db")
    temp_data = load_ship_data_from_db("shipsTemp.db")

    data_ships = []

    for ship in original_data.keys() & temp_data.keys():
        for component in ("weapon", "hull", "engine"):
            data_ships.append((
                ship,
                component,
                original_data[ship][component],
                temp_data[ship][component]
            ))

    metafunc.parametrize(
        "ship, ship_component, original_value, current_value",
        data_ships
    )


def load_ship_data_from_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    data = {}
    rows = cursor.execute("SELECT ship, weapon, hull, engine FROM Ships").fetchall()
    for row in rows:
        ship, weapon, hull, engine = row
        data[ship] = {
            "weapon": weapon,
            "hull": hull,
            "engine": engine
        }
    conn.close()
    return data

@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    for db_file in ["shipsOriginal.db", "shipsTemp.db"]:
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"Deleted {db_file}")


