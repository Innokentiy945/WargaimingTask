import random
import sqlite3

class DBOriginalInit:
    def __init__(self, connection):
        if not isinstance(connection, sqlite3.Connection):
            raise TypeError("connection must be an instance of sqlite3.Connection")
        self.conn = connection
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS weapons (
                weapon TEXT PRIMARY KEY,
                reload_speed INTEGER,
                rotational_speed INTEGER,
                diameter INTEGER,
                power_volley INTEGER,
                count INTEGER
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS hulls (
                hull TEXT PRIMARY KEY,
                armor INTEGER,
                type INTEGER,
                capacity INTEGER
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS engines (
                engine TEXT PRIMARY KEY,
                power INTEGER,
                type INTEGER
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ships (
                ship TEXT PRIMARY KEY,
                weapon TEXT,
                hull TEXT,
                engine TEXT,
                FOREIGN KEY (weapon) REFERENCES weapons(weapon),
                FOREIGN KEY (hull) REFERENCES hulls(hull),
                FOREIGN KEY (engine) REFERENCES engines(engine)
            );
        ''')

        self.conn.commit()

    def insert_to_weapons(self):
        for i in range(1, 21):
            weapon = f"Weapon-{i}"
            reload_speed = random.randint(1, 20)
            rotational_speed = random.randint(1, 20)
            diameter = random.randint(1, 20)
            power_volley = random.randint(1, 20)
            count = random.randint(1, 20)

            self.cursor.execute('''
                INSERT INTO weapons (weapon, reload_speed, rotational_speed, diameter, power_volley, count)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (weapon, reload_speed, rotational_speed, diameter, power_volley, count))

        self.conn.commit()
        print("Weapons original table populated.")

    def insert_to_hulls(self):
        for i in range(1, 6):
            hull = f"Hull-{i}"
            armor = random.randint(1, 20)
            type_ = random.randint(1, 20)  # избегаем совпадения с ключевым словом type
            capacity = random.randint(1, 20)

            self.cursor.execute('''
                INSERT INTO hulls (hull, armor, type, capacity)
                VALUES (?, ?, ?, ?)
            ''', (hull, armor, type_, capacity))

        self.conn.commit()
        print("Hulls original table populated.")

    def insert_to_engines(self):
        for i in range(1, 7):
            engine = f"Engine-{i}"
            power = random.randint(1, 20)
            type_ = random.randint(1, 20)

            self.cursor.execute('''
                INSERT INTO engines (engine, power, type)
                VALUES (?, ?, ?)
            ''', (engine, power, type_))

        self.conn.commit()
        print("Engines original table populated.")

    def insert_to_ships(self):
        for i in range(1, 201):
            ship_name = f"Ship-{i}"
            weapon_name = f"Weapon-{random.randint(1, 20)}"
            hull_name = f"Hull-{random.randint(1, 5)}"
            engine_name = f"Engine-{random.randint(1, 6)}"

            self.cursor.execute('''
                INSERT INTO Ships (ship, weapon, hull, engine)
                VALUES (?, ?, ?, ?)
            ''', (ship_name, weapon_name, hull_name, engine_name))

        self.conn.commit()
        print("Ships original table populated.")

    def close(self):
        self.conn.close()
