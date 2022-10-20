import mysql.connector

tuote_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)


mycursor = tuote_db.cursor() 

tuote = input("Kirjoita tuotteen nimi: ")
print(tuote)
hinta = input("Syötä hinta: ")
print(hinta)

mycursor = tuote_db.cursor() 
sql = f"INSERT INTO tuote (hinta, tuote) VALUES ({hinta},'{tuote}')"

mycursor.execute(sql)
tuote_db.commit()
tuote_db.close()
