from firebase_admin import credentials, firestore
import firebase_admin
import glob, rsa


firebase_admin.initialize_app(credentials.Certificate('./sa.json'))
db = firestore.client()
privKey = rsa.PrivateKey.load_pkcs1(open("privKey.pem", "rb").read())

def decryptRSA(key, encrypted_data):
    new_data = rsa.decrypt(encrypted_data,key)
    return new_data.decode()

def send_glob_to_firestore():
    files = glob.glob('Bytes/*.bytes')
    for file in files:
        with open(file, 'rb') as f:
            db.collection('Names Collected').document().set({"data": f.read()})
            print(f'Heres the data: {type(f.read())}')
            print(str(f))

def use_blobs():
    raw_data = db.collection('Names Collected').stream()
    data = []

    for doc in raw_data:
        file = doc.to_dict()
        stuff = decryptRSA(privKey, file["data"])
        # print(file["data"])
        data.append(stuff)
    print(data)

send_glob_to_firestore()
# use_blobs()
