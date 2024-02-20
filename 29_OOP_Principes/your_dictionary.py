class Translation:
    def __init__(self, word, translate):
        self.word = word
        self.translate = translate


class MyDict(Translation):
    def __init__(self, word, translate):
        super().__init__(word, translate)

    def Dictionary(self, dict_1) -> dict:
        dict_1[word] = translate
        return dict_1


dict_1 = {}
while True:
    word = input('Enter the word։ ')
    translate = input('access the literal translation : ')
    MyDict(word, translate).Dictionary(dict_1)
    if word == '0':
        break

check = input(
    'if you want to know, there is that word in the dictionary, enter the word, if you want to exit, press 0։')
if check in dict_1:
    print(dict_1[check])
else:
    print(0)
