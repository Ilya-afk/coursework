from PyQt5 import uic
from PyQt5 import QtCore, QtGui

current_table = 'user_data'

def get_user_data(sosi):
    print(sosi)
    return 'сработало'


test = f'get_{current_table}'

locals().get(test)
print(test)

print(locals()[test]('Gleb sosed'))
