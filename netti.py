import mysql.connector

netti_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)

mycursor = netti_db.cursor()

mycursor.execute("SELECT * FROM kayttaja")

print("asiakkaat")
myresult = mycursor.fetchall()
for x in myresult:
    print('nimi: ',x[2],'tilinumero: ',x[1])

netti_db.close()
