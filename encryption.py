def split(word):
    return [char for char in word]


def encrypt2(data):
    '''
    :param data: Data to encrypt
    :type data: str
    '''
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


print(decrypt([79, 75, 76, 71, 76, 82, 82, 71, 79, 81, 81, 73]))
