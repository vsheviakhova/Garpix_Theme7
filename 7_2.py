def read_lines(lines, file):
    with open(file) as f:
        content = f.readlines()
        content = reversed(content)
        counter = 0
        while counter < lines:
            for line in content:
                print(line.rstrip())
            counter += 1

read_lines(3, 'polozkova.txt')

with open ("polozkova.txt", "r") as BigFile:
    data=BigFile.readlines()
    for i in range(len(data)):
        print("Line No- ",i)
        print(data[i])


