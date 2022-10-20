import mysql.connector

tuote_db = mysql.connector.connect(
    host="127.0.0.1",
    user="nikopaasila",
    password="paasila",
    database="verkkokauppa"
)

mycursor = tuote_db.cursor()

mycursor.execute("SELECT * FROM tuote")

print("tuotteet")

myresult = mycursor.fetchall()
for x in myresult:
    print('tuote: ',x[1],'hinta: ',x[2])

    tuote_db.close()
