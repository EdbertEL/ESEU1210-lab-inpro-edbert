import mysql.connector as db

mydb = db.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud"
)

mycursor = mydb.cursor()

ID = input("Enter ID: ")
FirstName = input("Enter First Name: ")
LastName = input("Enter Last Name: ")
Address = input("Enter Address: ")
Telephone = input("Enter Telephone: ")
Email = input("Enter Email: ")
contacts = (ID, FirstName, LastName, Address, Telephone, Email)

sqlINSERT = "INSERT INTO contacts (ID, FirstName, LastName, Address, Telephone, Email) VALUES (%s, %s, %s, %s, %s, %s)"

mycursor.execute(sqlINSERT, contacts)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
# mycursor.close()
# mydb.close()