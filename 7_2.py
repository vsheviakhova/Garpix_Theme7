def read_lines(lines, file):
    with open(file) as f:
        content = f.readlines()
        i = -1
        while i >= -lines:
            print(content[i].rstrip())
            i -= 1
