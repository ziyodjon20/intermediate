import sqlite3

boglanish = sqlite3.connect("mydatabase.db")

cursor = boglanish.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS talabalar(
    ism TEXT,
    familiya TEXT,
    guruhi INTEGER
)         
               
               """)

cursor.execute("""
INSERT INTO talabalar VALUES
("Feruz", "Xoliqov", 208),
("Gulmurod", "Baymuratov", 207),
("Azamat", "Abdullayev", 209),
("Dilshod", "Sharipov", 208)
""")

cursor.execute("SELECT * FROM talabalar")

print(cursor.fetchall())