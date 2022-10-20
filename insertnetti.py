import mysql.connector

netti_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)
username = input("Kirjoita nimi: ")
print(username)
tilinumero = input("Syötä tilinumero: ")
print(tilinumero)

mycursor = netti_db.cursor() 
sql = f"INSERT INTO kayttaja (tilitiedot, nimi) VALUES ({tilinumero},'{username}')"


mycursor.execute(sql)
netti_db.commit()
netti_db.close()
