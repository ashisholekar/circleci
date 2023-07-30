def say_hello(name):

    print(f'Good Morning, {name}')


def to_upper(name):
    return name.upper()

if __name__ == '__main__':
    name = 'Pune'
    say_hello(name)
    up = to_upper(name)
    print(up)


