def read_poem(path):
    with open(path) as file:
        for i in range(6):
            print(file.readline().rstrip())

read_poem('polozkova.txt')