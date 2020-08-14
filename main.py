import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="tenantsdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tenants (name VARCHAR(255), house INTEGER(10))")

