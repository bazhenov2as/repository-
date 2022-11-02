def get_count_char(str_):
    str_ = str_.lower().split(' ')
    str_ = ''.join(str_)
    dictionary_ = {}

    for i in str_:
        if i.isalpha() and i not in dictionary_:
            dictionary_[i] = str_.count(i)
    return dictionary_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
dict = get_count_char(main_str)
def get_count2(dictionary_):
    list_ = {}
    bln = 0
    for key in dictionary_:
        bln += dictionary_[key]
    for k in dictionary_:
        list_[k] = int((dictionary_[k] / b) * 100)
    return list_
print(get_count2(dict))