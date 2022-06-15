def longest_word(path, word):
    with open(path) as f:
        content = f.read()
        #ниже я удаляю знаки пунктуации из строки и разделяю ее по пробелам на слова
        content = content.replace(',', '').\
            replace('.', '').\
            replace('!', '').\
            replace('?', '').\
            replace('(', '').\
            replace(')', '').\
            replace(' - ', '').\
            replace('\n', '')
        content = content.split(' ')

        counter = 0
        for i in content:
            if i.lower() == word.lower():
                counter += 1

    return counter
