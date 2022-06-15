def read_poem(path):
    with open(path) as file:
        counter = 0
        while counter < 6:
            print(file.readline().rstrip())
            counter += 1
