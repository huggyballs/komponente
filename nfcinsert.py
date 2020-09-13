import nfc
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="emovis",
    passwd="emovis",
    database="kontrolapristupa",
    autocommit=True
    )
mycursor = db.cursor()

try:
    #kod za dodavanje tablice s korisnicima
    mycursor.execute("CREATE TABLE UsersTest (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, Seclev ENUM('1', '2') NOT NULL, role VARCHAR(10) NOT NULL)")
    pass
except:
    print("postoji")
    pass
    #tablica postoji pa se ide dalje
try:
    mycursor.execute("CREATE TABLE DevicesTest (DeviceNum int PRIMARY KEY NOT NULL AUTO_INCREMENT, UserId int NOT NULL, DeviceId VARCHAR(40) NOT NULL)")
    pass
except:
    print("postoji")
    pass

clf = nfc.ContactlessFrontend()

clf.open('tty:AMA0')
assert clf.open('tty:AMA0') is True

try:
    mycursor.execute("INSERT INTO UsersTest (Seclev, role) VALUES (%s, %s)", (2, 'original'))
    lastrow = mycursor.lastrowid
    lastrow = int(lastrow)
    try:
        deviceId = clf.connect(rdwr={'on-connect': lambda tag: False})
        deviceId = str(deviceId)
        print(deviceId)

        mycursor.execute("INSERT INTO DevicesTest (UserId, DeviceId) VALUES (%s,%s)", (lastrow, deviceId))
        pass
    except:
        print("Nije uspjelo!")
    pass
except:
    print("Nije uspjelo! x2")
    pass
finally:
    clf.close()
    pass

mycursor.execute("SELECT * FROM UsersTest")
for x in mycursor:
    print(x)
mycursor.execute("SELECT * FROM DevicesTest")
for x in mycursor:
    print(x)

print("Sve super, program se zatvara!")