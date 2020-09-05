def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except Exception as err:
    print(str(err))
