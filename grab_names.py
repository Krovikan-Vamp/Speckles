import firebase_admin
from firebase_admin import credentials, firestore, storage
from firebase_admin import firestore

firebase_admin.initialize_app(credentials.Certificate(
    './sa.json'), {'storageBucket': 'fourpeaks-sc.appspot.com/Enc'})

bucket = storage.bucket()
db = firestore.client()
docs = db.collection(u'Auto Suggestions').stream()
new_arr = []
names = []

for doc in docs:
    new_arr.append(doc.to_dict())


def decrypt(data):
    arr = []
    for char in data:
        temp = int(char) - 25
        arr.append(chr(temp))
        # print(char)

    return ''.join(arr)


for n in new_arr:
    try:
        names.append(decrypt(n['n']))
    except KeyError:
        print('User has no name')

with open("output_names.txt", "wb") as f:
    for name in names:
        print(f'User: {name}')
        print(f'Encoded: {name.encode()}')
        f.write(f'{name}\n')
    f.close()
# print(names)
