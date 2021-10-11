import sqlite3, csv
conn = sqlite3.connect("insurance.db")
cur = conn.cursor()

#age, sex, bmi, children, smoker, region, charges
sql = """
    CREATE TABLE InsuaranceTable(
        ID INTEGER PRIMARY KEY,
        age INTEGER,
        sex TEXT,
        bmi FLOAT,
        children INTEGER,
        smoker TEXT,
        region TEXT,
        charges FLOAT
        );"""

cur.execute(sql)
print("DATABASE has been created.")

conn.commit()
conn.close()