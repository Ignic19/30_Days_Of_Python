#Writ a function which generates a six digit/character random_user_id.
# print(random_user_id())
#  '1ee33d'

#from random import random

#def generate_full_name(firstname, lastname):
#    return firstname + ' ' + lastname
#print(random_user_id());
  #'1ee33d'

import random
import string

def generate_id():
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return id

print(generate_id())