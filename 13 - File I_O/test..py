from turtle import mode
from translate import Translator
translator = Translator(to_lang="ja")


with open('./test.txt', mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
    with open('./test2.txt', mode='a') as my_file2:
        my_file2.write(translation)
