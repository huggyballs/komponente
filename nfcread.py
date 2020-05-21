import nfc
from nfc.clf import RemoteTarget

clf = nfc.ContactlessFrontend()

target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
print(target)
tag1 = nfc.tag.activate(clf, target)
print(tag1)
tag2 = clf.connect(rdwr={'on-connect': lambda tag: False})
print(tag2)
tag3 = clf.connect(rdwr={'on-connect': lambda tag: True})
print(tag3)
print("Gotovo je gotovo!")