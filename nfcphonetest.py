import nfc

clf = nfc.ContactlessFrontend()
clf.open('ttyAMA0')

try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    print(tag)
    print("Uspjesno citanje!")
except TimeoutError:
    print("Neuspjesno citanje!")
finally:
    clf.close()
    print("Gotovo je gotovo!")