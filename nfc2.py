import nfc
from nfc.clf import RemoteTarget

clf = nfc.ContactlessFrontend()
assert clf.open('tty:AMA0') is True
clf.close

target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
print(target)
tag = nfc.tag.activate(clf, target)
print(tag)

print("Kraj")