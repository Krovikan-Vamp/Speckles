import pyperclip as pc


def split(word):
    return [char for char in word]


def encrypt(data):
    arr = []
    split_data = split(data)

    for char in split_data:
        new_char = ord(char) + 25
        # new_char.to_bytes(len(char), 'little')
        arr.append(str(new_char.to_bytes(len(char), 'little')))
    arr = ''.join(arr)
    pc.copy(arr)

    return f'{data} >>>> {arr}'


def encrypt2(data):
    arr = []
    chars = split(data)

    for char in chars:
        arr.append(ord(char) + 25)

    return f'{data} >>>> {arr}'


def decrypt(data):
    arr = []

    for char in data:
        temp = int(char) - 25
        arr.append(chr(temp))
        # print(char)

    return f'{data} >>>> {"".join(arr)}'


print(encrypt2("623.399.6880"))
