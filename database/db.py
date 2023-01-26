import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1512",
  database="agilim"
)

mycursor = mydb.cursor()

# CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(1255), email VARCHAR(1255);
# CREATE TABLE users (ID int, name varchar(255), email varchar(255))
def init_user_dataBase(tableName):
    mycursor.execute(
        "CREATE TABLE " + tableName + " (id INT AUTO_INCREMENT PRIMARY KEY,"
        "name VARCHAR(1255),"
        "email VARCHAR(1255))"
        )

def add(val, tableName):
    sql = "INSERT INTO " + tableName + " (name, email) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()


if __name__ == '__main__':
    init_user_dataBase("users")
    val = ("pedro", "p@net.com")
    add(val, "users")


# CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(1255), email VARCHAR(1255);