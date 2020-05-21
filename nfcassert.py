import nfc

clf = nfc.ContactlessFrontend()
assert clf.open('tty:AMA0') is True
print("Obavljeno!")
clf.close()