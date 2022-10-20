import mysql.connector

kori_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)

mycursor = kori_db.cursor()

mycursor.execute("SELECT kayttaja.nimi, tuote.tuote, tuote.hinta FROM kayttaja, tuote, ostoskori WHERE kayttaja.kayttajaid = ostoskori.kayttajaid AND tuote.id = ostoskori.tuoteid")


myresult = mycursor.fetchall()
for x in myresult:
    print('tuote: ',x[1],'käyttäjä: ',x[0],'hinta: ',x[2])

    kori_db.close()
