def split(word):
    return [char for char in word]


def encrypt(data):
    encrypted_data = []
    data = split(data)

    for n in data:
        initial = ord(n) + 13
        new_val = initial.to_bytes()
        encrypted_data.append(new_val.to_bytes(1, 'little'))
        
    real_data = ''.join(encrypted_data)
    return real_data

# def decrypt(data):

#     return decrypted_data
print(encrypt('this thing'))