def longest_word(path):
    with open(path) as f:
        content = f.read()
        content = content.replace(',', '').\
            replace('.', '').\
            replace('!', '').\
            replace('?', '').\
            replace('(', '').\
            replace(')', '').\
            replace(' - ', '').\
            replace('\n', '')
        content = content.split(' ')
        words_len = []
        for i in content:
            words_len.append(len(i))

        longest_list = []
        for i in content:
            if len(i) == max(words_len):
                longest_list.append(i)

    return longest_list
