import nfc
from nfc.clf import RemoteTarget

clf.open
clf = nfc.ContactlessFrontend()
assert clf.open('tty:AMA0') is True
clf.close

target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
print(target)
tag = nfc.tag.activate(clf, target)
print(tag)
tag2 = clf.connect(rdwr={'on-connect': lambda tag: False})
print(tag2)
tag3 = clf.connect(rdwr={'on-connect': lambda tag: True})
print(tag3)
clf.close

print("Kraj")