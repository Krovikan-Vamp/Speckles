from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

firebase_admin.initialize_app(credentials.Certificate('./sa.json'))
db = firestore.client()

raw_docs = db.collection(u'Testimonials').stream()
docs = []
suggestion_list = []

for doc in raw_docs:
    docs.append(doc.to_dict())

for testimonial in docs:
    # print(testimonial)
    split = testimonial['comments'].split(' ')
    for word in split:
        try:
            suggestion_list.index(word)
        except ValueError:
            suggestion_list.append(word)
            pass

# print(suggestion_list)

test = {'test': ['<html>', '<body>', '<head>', '<title>']}
text = prompt(f'>>  ', completer=WordCompleter(test['test']))
print('You said: %s' % text)
