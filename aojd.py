mylist = ['1', '2', '3']

try:
     mylist.index('9')
except ValueError:
    print('Yep, its a ValueError')