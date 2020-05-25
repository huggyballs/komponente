import nfc

clf = nfc.ContactlessFrontend()
clf.open('ttyAMA0')

try:
    tag = clf.connect(llcp ={})
    print(tag)
    print("Uspjesno citanje!")
except:
    print("Neuspjesno citanje!")
finally:
    clf.close()
    print("Gotovo je gotovo!")