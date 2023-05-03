def outer(msg):
    lang = 'Python'

    def inner():
        print(lang, msg)
        return inner


my_func = outer('is fun!!!')
my_func()  # output: 'Python is fun!!!'
