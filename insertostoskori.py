import mysql.connector

kori_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)

mycursor = kori_db.cursor() 

kayttajaid = input("Kirjoita käyttäjän id: ")
print(kayttajaid)
tuoteid = input("Syötä tuotteen id: ")
print(tuoteid)

mycursor = kori_db.cursor() 
sql = f"INSERT INTO ostoskori (kayttajaid, tuoteid) VALUES ({kayttajaid},'{tuoteid}')"

mycursor.execute(sql)
kori_db.commit()
kori_db.close()
