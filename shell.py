import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    print(error)
    if error:
        print('error detected')
        print(error.as_string())
        print('error proccessed')
    else: print(result)