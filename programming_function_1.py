### 函数返回

def sing():
    return('happy birthday to you\n')

def person(name):
    return(sing()*2 +'happy birthday to dear {}\n'.format(name)+sing())

def main():
    name = input('pleas input your name:')
    print(person(name))

main()